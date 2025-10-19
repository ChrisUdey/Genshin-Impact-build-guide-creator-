import requests
import sys
import os

# Add parent directory to path so we can import from app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal, Base, engine
from app.models import Character  # Import all models
from datetime import datetime


def seed_characters():
    """Fetch characters from Genshin API and seed database"""

    # Create all tables
    print(" Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print(" Database tables created")

    db = SessionLocal()

    try:
        # Check if characters already exist
        existing_count = db.query(Character).count()
        if existing_count > 0:
            print(f"⚠️  Characters already seeded ({existing_count} characters found)")
            response = input("Delete and re-seed? (yes/no): ")
            if response.lower() != 'yes':
                print("Aborting seed.")
                return
            # Delete existing characters
            db.query(Character).delete()
            db.commit()
            print(" Deleted existing characters")

        print(" Fetching characters from Genshin API...")

        # Fetch character list
        response = requests.get('https://genshin.jmp.blue/characters')
        character_keys = response.json()

        print(f" Found {len(character_keys)} characters")

        characters_added = 0

        # Fetch each character's details
        for key in character_keys:
            try:
                print(f"   Fetching {key}...")
                char_response = requests.get(f'https://genshin.jmp.blue/characters/{key}')
                char_data = char_response.json()

                # Parse birthday (format: "0000-MM-DD")
                birthday_str = char_data.get('birthday', '0000-01-01')

                # Parse release date if available
                release_str = char_data.get('release')
                release_date = None
                if release_str:
                    try:
                        release_date = datetime.strptime(release_str, '%Y-%m-%d').date()
                    except:
                        pass

                # Create character
                character = Character(
                    name=char_data.get('name'),
                    title=char_data.get('title'),
                    vision=char_data.get('vision'),
                    weapon=char_data.get('weapon'),
                    gender=char_data.get('gender'),
                    nation=char_data.get('nation'),
                    affiliation=char_data.get('affiliation'),
                    rarity=char_data.get('rarity'),
                    release=release_date,
                    constellation=char_data.get('constellation'),
                    birthday=birthday_str,
                    description=char_data.get('description')
                )

                db.add(character)
                characters_added += 1

            except Exception as e:
                print(f"     Error fetching {key}: {str(e)}")
                continue

        db.commit()
        print(f"\n Successfully seeded {characters_added} characters!")

    except Exception as e:
        print(f"\n Error: {str(e)}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_characters()