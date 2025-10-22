from app.database import SessionLocal
from app.models import BuildGuide

db = SessionLocal()
print(db.query(BuildGuide).all())
db.close()
