from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String,unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

# This class is derived from Base, linking it to the database schema defined in database.py.

class Todos(Base):
    __tablename__ = 'todos'  #explicit table name
    # __tablename__ is the standard naming convention in SQLAlchemy when using the declarative ORM model.

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Integer)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))


