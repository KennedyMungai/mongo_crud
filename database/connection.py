"""This script hand;es database connections"""
from sqlmodel import SQLModel, Session, create_engine
from models.events import Event


database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connection_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string,
                           echo=True, connection_args=connection_args)


def conn():
    """Connection function"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """Session function"""
    with Session(engine_url) as session:
        yield session
