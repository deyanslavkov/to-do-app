from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        tags=','.join(task.tags) if task.tags else ''
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_active_tasks(db: Session):
    return db.query(Task).filter(Task.is_completed == False).all()

def get_archived_tasks(db: Session):
    return db.query(Task).filter(Task.is_completed == True).all()

def complete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.is_completed = True
        db.commit()
        db.refresh(task)
    return task