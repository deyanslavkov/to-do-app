"""
Todo endpoints module.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.services.todo import TodoService

router = APIRouter()


@router.get("/", response_model=List[TodoResponse])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all todos.

    Args:
        skip: Number of records to skip.
        limit: Maximum number of records to return.
        db: Database session.

    Returns:
        List of todos.
    """
    todo_service = TodoService(db)
    return todo_service.get_todos(skip=skip, limit=limit)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Get a specific todo by ID.

    Args:
        todo_id: ID of the todo to retrieve.
        db: Database session.

    Returns:
        Todo details.

    Raises:
        HTTPException: If todo not found.
    """
    todo_service = TodoService(db)
    todo = todo_service.get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return todo


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """
    Create a new todo.

    Args:
        todo: Todo data.
        db: Database session.

    Returns:
        Created todo.
    """
    todo_service = TodoService(db)
    return todo_service.create_todo(todo)


@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    """
    Update a todo.

    Args:
        todo_id: ID of the todo to update.
        todo: Todo data to update.
        db: Database session.

    Returns:
        Updated todo.

    Raises:
        HTTPException: If todo not found.
    """
    todo_service = TodoService(db)
    updated_todo = todo_service.update_todo(todo_id, todo)
    if updated_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    Delete a todo.

    Args:
        todo_id: ID of the todo to delete.
        db: Database session.

    Raises:
        HTTPException: If todo not found.
    """
    todo_service = TodoService(db)
    deleted = todo_service.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
