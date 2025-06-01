"""
Tests for todo endpoints.
"""

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.models.todo import Todo


def test_create_todo(client, db_session):
    """Test creating a todo."""
    response = client.post(
        "/api/todos/",
        json={"title": "Test todo", "completed": False},
    )

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Test todo"
    assert data["completed"] is False
    assert "id" in data

    # Check if todo was actually created in DB
    todo = db_session.query(Todo).filter(Todo.id == data["id"]).first()
    assert todo is not None
    assert todo.title == "Test todo"


def test_get_todos(client, db_session):
    """Test getting all todos."""
    # Create some test todos
    todo1 = Todo(title="Test todo 1", completed=False)
    todo2 = Todo(title="Test todo 2", completed=True)
    db_session.add_all([todo1, todo2])
    db_session.commit()

    response = client.get("/api/todos/")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) >= 2

    # Verify specific todos are in the response
    todo_ids = [todo["id"] for todo in data]
    assert todo1.id in todo_ids
    assert todo2.id in todo_ids


def test_get_todo(client, db_session):
    """Test getting a specific todo."""
    todo = Todo(title="Test todo", completed=False)
    db_session.add(todo)
    db_session.commit()

    response = client.get(f"/api/todos/{todo.id}")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == todo.id
    assert data["title"] == "Test todo"
    assert data["completed"] is False


def test_get_nonexistent_todo(client):
    """Test getting a nonexistent todo."""
    response = client.get("/api/todos/9999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_todo(client, db_session):
    """Test updating a todo."""
    todo = Todo(title="Original todo", completed=False)
    db_session.add(todo)
    db_session.commit()

    response = client.patch(
        f"/api/todos/{todo.id}",
        json={"title": "Updated todo", "completed": True},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["title"] == "Updated todo"
    assert data["completed"] is True

    # Check if todo was actually updated in DB
    db_session.refresh(todo)
    assert todo.title == "Updated todo"
    assert todo.completed is True


def test_update_nonexistent_todo(client):
    """Test updating a nonexistent todo."""
    response = client.patch(
        "/api/todos/9999",
        json={"title": "Updated todo", "completed": True},
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_todo(client, db_session):
    """Test deleting a todo."""
    todo = Todo(title="Test todo", completed=False)
    db_session.add(todo)
    db_session.commit()

    response = client.delete(f"/api/todos/{todo.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Check if todo was actually deleted from DB
    todo = db_session.query(Todo).filter(Todo.id == todo.id).first()
    assert todo is None


def test_delete_nonexistent_todo(client):
    """Test deleting a nonexistent todo."""
    response = client.delete("/api/todos/9999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
