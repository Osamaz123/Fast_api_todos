from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, Path
import models
from models import Todos
from database import engine, SessionLocal
from starlette import status

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

@app.get("/", status_code=status.HTTP_200_OK)
# Depends is dependency injection
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found.')