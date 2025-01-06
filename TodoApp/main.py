from fastapi import FastAPI
import models
from database import engine

app = FastAPI()


# Generates the necessary database schema based on the ORM models defined in models.py.
# Creates the todos table in the SQLite database (todos.db) if it does not already exist.
models.Base.metadata.create_all(bind= engine)