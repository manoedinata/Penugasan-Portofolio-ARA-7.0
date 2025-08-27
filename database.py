from sqlmodel import SQLModel, Session, create_engine
from typing import Annotated
from fastapi import Depends

# Database setup
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# Function: Initialize DB
# FIXME: This will be unneeded when Alembic is used
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Function: Yield database session
def get_session():
    with Session(engine) as session:
        yield session

# Dependencies: Database session
SessionDep = Annotated[Session, Depends(get_session)]
