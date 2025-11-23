from app.database import SessionLocal
from app.models.domain_artifact import DomainArtifact

db = SessionLocal()

links = [
    DomainArtifact(domain_id=1, artifact_id="adventurer"),
    DomainArtifact(domain_id=1, artifact_id="teacher"),
    DomainArtifact(domain_id=1, artifact_id="gladiators-finale"),
]

db.add_all(links)
db.commit()
db.close()

print("Seeded domain artifacts!")
