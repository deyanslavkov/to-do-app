from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskOut
from app.crud.task import create_task, get_active_tasks, get_archived_tasks, complete_task
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/", response_model=List[TaskOut])
def get_all(db: Session = Depends(get_db)):
    return get_active_tasks(db)

@router.get("/archive", response_model=List[TaskOut])
def get_archive(db: Session = Depends(get_db)):
    return get_archived_tasks(db)

@router.post("/complete/{task_id}", response_model=TaskOut)
def complete(task_id: int, db: Session = Depends(get_db)):
    task = complete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task