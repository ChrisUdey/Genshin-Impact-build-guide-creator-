from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .database import engine, Base
from .routes import characters, auth, build_guides
from .config import settings
import os

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Genshin Build Guide API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded files
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(build_guides.router)
app.include_router(characters.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Genshin Build Guide API"}