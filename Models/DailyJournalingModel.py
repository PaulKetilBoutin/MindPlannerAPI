from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from Models import OpenCyclesModel

class DailyJournaling(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    comment: str = Field(default=None)
    journalingDate: str | None = Field(default_factory=datetime.now().strftime("%c"))
    proudMetter: int = Field(default=None)
