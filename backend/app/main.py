"""
Main application module for the Todo API.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title="Todo API",
    description="API for managing todos",
    version="0.1.0",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,  # type: ignore[arg-type]
    allow_credentials=True,  # type: ignore[arg-type]
    allow_methods=["*"],  # type: ignore[arg-type]
    allow_headers=["*"],  # type: ignore[arg-type]
)

# Include API router
app.include_router(api_router, prefix="/api")

print("CORS_ORIGINS raw:", os.getenv("CORS_ORIGINS"))


@app.get("/")
async def root():
    """Root endpoint that redirects to API documentation."""
    return {"message": "Welcome to Todo API. Go to /docs for API documentation."}
