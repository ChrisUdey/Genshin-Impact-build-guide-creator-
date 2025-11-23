from scripts.seed_artifacts import seed_artifacts
from scripts.seed_build_guides import seed_build_guides
from scripts.seed_characters import seed_characters
from scripts.seed_domain_artifacts import seed_domain_artifacts
from scripts.seed_domains import seed_domains
from app.database import Base, engine
if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    seed_characters()
    seed_build_guides()
    seed_artifacts()
    seed_domains()
    seed_domain_artifacts()