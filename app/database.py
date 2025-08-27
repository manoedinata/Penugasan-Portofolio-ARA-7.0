from sqlmodel import SQLModel, Session, create_engine
from typing import Annotated
from fastapi import Depends

from settings import settings

# Database setup
if settings.database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}
engine = create_engine(settings.database_url, connect_args=connect_args)

# Function: Yield database session
def get_session():
    with Session(engine) as session:
        yield session

# Dependencies: Database session
SessionDep = Annotated[Session, Depends(get_session)]
