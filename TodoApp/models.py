from database import Base
from sqlalchemy import Column, Integer, String, Boolean


# This class is derived from Base, linking it to the database schema defined in database.py.

class Todos(Base):
    __tablename__ = 'todos'  #explicit table name
    # __tablename__ is the standard naming convention in SQLAlchemy when using the declarative ORM model.

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Integer)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)


