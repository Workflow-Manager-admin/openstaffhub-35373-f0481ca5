from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routes import router

openapi_tags = [
    {
        "name": "employees",
        "description": "Operations with employees.",
    },
    {
        "name": "departments",
        "description": "Operations with departments.",
    },
    {
        "name": "positions",
        "description": "Operations with job positions.",
    },
]

app = FastAPI(
    title="Employment Management System API",
    description="Backend API for managing employees, departments, and job positions.",
    version="1.0.0",
    openapi_tags=openapi_tags,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")


def on_startup():
    # Create all tables (safe to run even if tables already exist)
    Base.metadata.create_all(bind=engine)


@app.get("/", tags=["health"])
def health_check():
    """Basic health check endpoint."""
    return {"message": "Healthy"}


app.include_router(router, tags=["departments", "positions", "employees"])
