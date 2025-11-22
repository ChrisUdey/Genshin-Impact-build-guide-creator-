import requests
from app.database import SessionLocal, Base, engine
from app.models.domain import Domain


def seed_domains():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        resp = requests.get("https://genshin.jmp.blue/domains/all?lang=en")
        resp.raise_for_status()
        domains = resp.json()

        for d in domains:
            # Use .get() with default None for missing fields
            name = d.get("name")
            domain_type = d.get("type")
            description = d.get("description")
            location = d.get("location")
            nation = d.get("nation")
            picture_path = f"nation_pics/{nation}/icon.png".lower()


            # Check if domain already exists
            domain = db.query(Domain).filter(Domain.name == name).first()
            if not domain:
                domain = Domain(
                    name=name or None,
                    type=domain_type or None,
                    description=description or None,
                    location=location or None,
                    nation=nation or None,
                    picture_path=picture_path or None,
                )
                db.add(domain)

        db.commit()
        print("Domains seeded successfully!")

    except Exception as e:
        print("Error seeding domains:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_domains()
