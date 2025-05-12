# fastAPI\crud_todo\schemas.py
from pydantic import BaseModel

# Create Task schema (Pydantic Model)
class TaskCreate(BaseModel):
    task: str

# Full Task schema (Pydantic Model)
class Task(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True