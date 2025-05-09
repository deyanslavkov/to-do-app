"""
Todo repository for database access.
"""

from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.repositories.base import BaseRepository


class TodoRepository(BaseRepository[Todo]):
    """Todo repository for database access."""

    def __init__(self, db: Session):
        """
        Initialize repository with database session.

        Args:
            db: Database session.
        """
        super().__init__(Todo, db)
