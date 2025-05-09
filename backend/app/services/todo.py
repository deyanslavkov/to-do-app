"""
Todo service for business logic.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.repositories.todo import TodoRepository
from app.schemas.todo import TodoCreate, TodoUpdate


class TodoService:
    """Todo service for business logic."""

    def __init__(self, db: Session):
        """
        Initialize service with database session.

        Args:
            db: Database session.
        """
        self.repository = TodoRepository(db)

    def get_todos(self, skip: int = 0, limit: int = 100):
        """
        Get all todos with pagination.

        Args:
            skip: Number of records to skip.
            limit: Maximum number of records to return.

        Returns:
            List of todos.
        """
        return self.repository.get_all(skip=skip, limit=limit)

    def get_todo_by_id(self, todo_id: int):
        """
        Get a specific todo by ID.

        Args:
            todo_id: ID of the todo to retrieve.

        Returns:
            Todo if found, None otherwise.
        """
        return self.repository.get(todo_id)

    def create_todo(self, todo: TodoCreate):
        """
        Create a new todo.

        Args:
            todo: Todo data.

        Returns:
            Created todo.
        """
        return self.repository.create(todo)

    def update_todo(self, todo_id: int, todo: TodoUpdate):
        """
        Update a todo.

        Args:
            todo_id: ID of the todo to update.
            todo: Todo data to update.

        Returns:
            Updated todo if found, None otherwise.
        """
        return self.repository.update(todo_id, todo)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo.

        Args:
            todo_id: ID of the todo to delete.

        Returns:
            True if todo was deleted, False if not found.
        """
        return self.repository.delete(todo_id)
