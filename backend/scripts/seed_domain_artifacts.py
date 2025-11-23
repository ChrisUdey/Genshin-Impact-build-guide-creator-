from app.database import SessionLocal
from app.models.domain import Domain
from app.models.artifact import Artifact
from app.models.domain_artifact import DomainArtifact

def seed_domain_artifacts():
    db = SessionLocal()

    try:
        # Get all domains & artifacts
        domains = db.query(Domain).order_by(Domain.id).all()
        artifacts = db.query(Artifact).order_by(Artifact.artifactID).all()

        if not artifacts:
            print("No artifacts found!")
            return

        print(f"Found {len(domains)} domains and {len(artifacts)} artifacts")

        # Clear old links
        db.query(DomainArtifact).delete()
        db.commit()

        artifact_index = 0  # Start at first artifact

        links = []

        for domain in domains:
            # Pick 3 artifacts for this domain
            selected = []
            for _ in range(3):
                selected.append(artifacts[artifact_index % len(artifacts)])
                artifact_index += 1

            # Make DomainArtifact entries
            for art in selected:
                links.append(
                    DomainArtifact(
                        domain_id=domain.id,
                        artifact_id=art.artifactID
                    )
                )

        db.add_all(links)
        db.commit()
        print("Seeded domain artifacts successfully!")

    except Exception as e:
        print("Error seeding domain artifacts:", e)
        db.rollback()

    finally:
        db.close()
