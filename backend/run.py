import uvicorn

from scripts.seed_all import seed_all

if __name__ == "__main__":
    seed_all()
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)