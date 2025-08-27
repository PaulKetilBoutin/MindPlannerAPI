from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from Models import OpenCyclesModel

class DailyQuests(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    expecetedDuration: int = Field(default=None)
    openCycle_id: int | None = Field(default=None)
    nbrOfRep: int | None = Field(default=0)
#    dateLastRep: str | None = Field(default_factory=datetime.now().strftime("%c"))
