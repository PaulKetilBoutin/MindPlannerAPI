from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select

class OpenCycles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tite: str = Field(index=True)
    endTimeStamp: str = Field(default=None)
    progression: int | None = Field(default=0)

