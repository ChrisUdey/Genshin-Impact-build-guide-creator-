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
    domain = db.query(Domain).filter(Domain.id == domain_id).first()
    if not domain:
        raise HTTPException(status_code=404, detail="Domain not found")
    return domain

