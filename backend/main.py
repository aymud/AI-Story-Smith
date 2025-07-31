from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import create_tables
from routers import story, job
from core.config import settings

create_tables()

app = FastAPI(
    title="Choose Your Own Adventure Game API",
    description="API to generate stories for a choose your own adventure game.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Allows API to be accessed from a different origin (URL/domain you are running the frontend on).
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect the routers to the application.
app.include_router(story.router, prefix=settings.API_PREFIX)
app.include_router(job.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)