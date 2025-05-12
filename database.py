# fastAPI\crud_todo\database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of SQLite engine
engine = create_engine("sqlite:///fastapidb.db")

# Create an instance of DeclarativeMeta
Base = declarative_base()

# Create the SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)