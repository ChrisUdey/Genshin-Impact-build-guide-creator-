from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.database import get_db
from app.models import DomainArtifact
from app.models.domain import Domain
from app.schemas.domain import DomainResponse

router = APIRouter(prefix="/api/domains", tags=["Domains"])

@router.get("/", response_model=list[DomainResponse])
async def get_domains(db: Session = Depends(get_db)):
    domains = db.query(Domain).all()
    return domains

@router.get("/{domain_id}", response_model=DomainResponse)
def get_domain(domain_id: int, db: Session = Depends(get_db)):
    domain = (
        db.query(Domain)
        .options(
            joinedload(Domain.artifacts).joinedload(DomainArtifact.artifact)
        )
        .filter(Domain.id == domain_id)
        .first()
    )
    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")

    return domain


@router.post("/reload/{domain_id}", response_model=DomainResponse)
def reload_domain(domain_id: int, db: Session = Depends(get_db)):
    """
    Reload a single domain from upstream WITHOUT changing its ID
    and WITHOUT touching the existing artifact links.

    - Keeps Domain.id the same (so front-end routes still work)
    - Updates type / description / location / nation / image
    - Leaves DomainArtifact rows as-is (same 3 artifacts as before)
    """
    # Load domain (with artifacts) from DB
    domain = (
        db.query(Domain)
        .options(
            joinedload(Domain.artifacts).joinedload(DomainArtifact.artifact)
        )
        .filter(Domain.id == domain_id)
        .first()
    )

    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")

    # Fetch latest domain data from upstream API
    import requests

    resp = requests.get("https://genshin.jmp.blue/domains/all?lang=en")
    resp.raise_for_status()
    all_domains = resp.json()

    # Match the domain by name (same as initial seeding)
    upstream = next((d for d in all_domains if d.get("name") == domain.name), None)
    if not upstream:
        raise HTTPException(status_code=500, detail="Upstream domain not found")

    # Update domain fields in-place (keep same ID)
    domain.type = upstream.get("type") or domain.type
    domain.description = upstream.get("description") or domain.description
    domain.location = upstream.get("location") or domain.location
    domain.nation = upstream.get("nation") or domain.nation

    nation = upstream.get("nation")
    if nation:
        domain.image = f"nation_pics/{nation}/icon.png"

    db.commit()
    db.refresh(domain)

    # Return with artifacts eagerly loaded
    return domain
