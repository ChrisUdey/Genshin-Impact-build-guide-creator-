import requests

from app.database import Base, engine, SessionLocal

# Import ALL MODELS (must be imported so metadata knows tables)
from app.models.artifact import Artifact
from app.models.domain_artifact import DomainArtifact
from app.models.domain import Domain


def seed_domains():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        print("Fetching domains from API...")
        resp = requests.get("https://genshin.jmp.blue/domains/all?lang=en")
        resp.raise_for_status()
        domains = resp.json()

        for d in domains:
            name = d.get("name")
            nation = d.get("nation") or "Unknown"

            # Check if domain already exists
            existing_domain = db.query(Domain).filter(Domain.name == name).first()
            if existing_domain:
                print(f"Skipping existing domain: {name}")
                continue

            # Create domain
            domain = Domain(
                name=name,
                type=d.get("type"),
                description=d.get("description"),
                location=d.get("location"),
                nation=nation,
                image=f"nation_pics/{nation}/icon.png",
            )

            db.add(domain)
            db.flush()  # ensures domain.id is available

            # Add artifact drop pool
            drop_pool = d.get("drop", [])

            for art in drop_pool:
                raw_artifact_id = art.get("id")

                if not raw_artifact_id:
                    continue

                # Convert artifact ID from API format → DB format:
                # "gladiators_finale" → "gladiators-finale"
                artifact_id = raw_artifact_id.lower().replace("_", "-")

                # Check artifact exists
                artifact = db.query(Artifact).filter(Artifact.artifactID == artifact_id).first()

                if not artifact:
                    print(f"⚠ WARNING: Artifact not found in DB: {artifact_id}")
                    continue

                # Prevent duplicate domain-artifact entries
                existing_link = db.query(DomainArtifact).filter(
                    DomainArtifact.domain_id == domain.id,
                    DomainArtifact.artifact_id == artifact_id
                ).first()

                if existing_link:
                    continue

                # Create link
                db.add(DomainArtifact(
                    domain_id=domain.id,
                    artifact_id=artifact_id
                ))

        db.commit()
        print("Domains & artifact associations seeded successfully!")

    except Exception as e:
        print("Error seeding domains:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_domains()
