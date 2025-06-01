"""
Todo Pydantic schemas for request/response validation.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    """Base Todo schema."""

    title: str = Field(..., min_length=1, max_length=100, example="Buy groceries")
    completed: bool = Field(default=False, example=False)


class TodoCreate(TodoBase):
    """Todo create schema."""

    pass


class TodoUpdate(BaseModel):
    """Todo update schema."""

    title: Optional[str] = Field(
        None, min_length=1, max_length=100, example="Buy more groceries"
    )
    completed: Optional[bool] = Field(None, example=True)


class TodoResponse(TodoBase):
    """Todo response schema."""

    id: int
    created_at: datetime

    class Config:
        """Pydantic config."""

        from_attributes = True
