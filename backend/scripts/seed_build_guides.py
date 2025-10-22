import sys
import os
import random
from datetime import datetime

# Add parent directory to path so we can import from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, Base, engine
from app.models import BuildGuide, Character


def seed_build_guides():
    """Seed example build guides for existing characters."""

    print(" Creating database tables (if not exist)...")
    Base.metadata.create_all(bind=engine)
    print(" Database tables ready.")

    db = SessionLocal()


    try:
        # Check for existing build guides
        existing_count = db.query(BuildGuide).count()
        if existing_count > 0:
            print(f" Build guides already seeded ({existing_count} found).")
            response = input("Delete and re-seed? (yes/no): ")
            if response.lower() != "yes":
                print("Aborting seed.")
                return

            db.query(BuildGuide).delete()
            db.commit()
            print(" Deleted existing build guides.")


        guides_added = 0

        for guide in premade_guides():
            db.add(guide)
            guides_added += 1

        db.commit()
        print(f"\n Successfully seeded {guides_added} build guides!")

    except Exception as e:
        print(f"\n Error: {str(e)}")
        import traceback
        traceback.print_exc()
        db.rollback()

    finally:
        db.close()


def premade_guides():
    guide1 = BuildGuide(
        username="ChrisU",
        character_id= "1",
        title="Build Guide",
        description=(
            "IM THE BEST PLAYER IN NORTH AMERICA! and this guide covers the optimal build for Albedo. Make sure you build him on defensive artifacts"
            "to maximize his damage output off-field, also focus on giving him at least 150% energy recharge for optimal"
            "rotations "
        ),
        picture_path="build_pics/albedoguidechris.png",
        created_at=datetime.utcnow()
    )
    guide2 = BuildGuide(
        username="NoobMaster",
        character_id= "92",
        title="Build Guide",
        description=(
            "I want to let everyone know that we've been building Zhongli WRONG!!!"
            "Although his stats scaling suggest defence to be his best stat, his shield scales hp"
            "With just 40000 HP Zhongli's shield becomes unbreakable!"
        ),
        picture_path="build_pics/zhonglibuildguide2.jpg",
        created_at=datetime.utcnow()
    )

    return guide1, guide2


if __name__ == "__main__":
    seed_build_guides()
