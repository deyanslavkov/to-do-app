from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = []

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    is_completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True