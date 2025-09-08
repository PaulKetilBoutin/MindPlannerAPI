from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select

class WishesCycles(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    endTimeStamp: str | None = Field(default=None)
    progression: int | None = Field(default=0)

