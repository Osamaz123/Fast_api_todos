from fastapi import Depends, FastAPI
import models
from database import engine
from routers import auth, todos,admin, users

app = FastAPI()


# Generates the necessary database schema based on the ORM models defined in models.py.
# Creates the todos table in the SQLite database (todos.db) if it does not already exist.
models.Base.metadata.create_all(bind= engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)


