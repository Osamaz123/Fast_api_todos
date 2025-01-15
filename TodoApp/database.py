from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'


# Creates a SQLAlchemy engine instance that serves as a factory for database connections.
# This is used to establish communication between SQLAlchemy and the SQLite database.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# bind=engine: Links the session to the engine, defining which database the session should connect to.
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
# Returns: A session object that can be used to query and manipulate the database.


# Provides a base class (Base) for creating ORM (Object Relational Mapping) models.
# Every database model (table) will inherit from this Base.
Base = declarative_base()