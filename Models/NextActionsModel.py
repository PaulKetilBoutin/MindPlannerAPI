from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from Models import OpenCyclesModel

class NextActions(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tite: str = Field(index=True)
    task: str = Field()
    motivation_min: int = Field(default=None)
    endTimeStamp: str = Field(default=None)
    openCycle_id: int = Field(default=None)
    done: bool = Field(default=False)
    link: str | None = Field(default=None)
    timeSensitive: str | None = Field(default=None)
    expected_duration: int = Field(default=None)
    real_duration: int = Field(default=0)
