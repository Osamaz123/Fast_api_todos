from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
import models
from models import Todos
from database import engine, SessionLocal

app = FastAPI()


# Generates the necessary database schema based on the ORM models defined in models.py.
# Creates the todos table in the SQLite database (todos.db) if it does not already exist.
models.Base.metadata.create_all(bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
# Depends is dependency injection
async def read_all(db: db_dependency):
    return db.query(Todos).all()