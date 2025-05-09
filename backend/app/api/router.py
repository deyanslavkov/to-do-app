"""
Main API router that includes all endpoint routers.
"""

from fastapi import APIRouter

from app.api.endpoints import todos

api_router = APIRouter()
api_router.include_router(todos.router, prefix="/todos", tags=["todos"])
