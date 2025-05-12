# crud/main.py
from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

Base.metadata.create_all(engine)  # Create the database

# Initialize the application
app = FastAPI()

# Helper function to get the database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def home():
    return "all"

@app.post("/todo", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, session: Session = Depends(get_session)):
    task_db = models.Task(task=task.task)

    session.add(task_db)
    session.commit()
    session.refresh(task_db)

    return task_db

@app.get("/todo/{id}", response_model=schemas.Task)
def read_task(id: int, session: Session = Depends(get_session)):
    task = session.query(models.Task).get(id)  # Get item with given id

    # Check if id exists. If not, return 404 not found response
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return task

@app.put("/todo/{id}", response_model=schemas.Task)
def update_task(id: int, task: str, session: Session = Depends(get_session)):
    task_db = session.query(models.Task).get(id)  # Get given id

    if task_db:
        task_db.task = task
        session.commit()

    # Check if id exists. If not, return 404 not found response
    if not task_db:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return task_db

@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, session: Session = Depends(get_session)):
    # Get given id
    task_db = session.query(models.Task).get(id)

    # If task with given id exists, delete it from the database. Otherwise, raise 404 error
    if task_db:
        session.delete(task_db)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    return None

@app.get("/todo", response_model=List[schemas.Task])
def read_task_list(session: Session = Depends(get_session)):
    task_list = session.query(models.Task).all()  # Get all tasks

    return task_list
