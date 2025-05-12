# fastAPI\crud_todo\models.py
from sqlalchemy import Column, Integer, String
from database import Base

# Define the Task class from Base
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))