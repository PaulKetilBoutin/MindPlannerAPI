from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from Models import OpenCyclesModel

class NextActions(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    task: str = Field()
    motivation_mini: int = Field(default=None)
    endTimeStamp: str | None = Field(default=None)
    openCycle_id: int | None = Field(default=None)
    done: bool = Field(default=False)
    timeSensitive: str | None = Field(default=None)
    expected_duration: int = Field(default=None)
    real_duration: int = Field(default=0)
