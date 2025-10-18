from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import characters
from .config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Genshin Build Guide API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                    "http://localhost:3001",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(characters.router)

@app.get("/")
async def root():
    return {"message": "Genshin Build Guide API"}