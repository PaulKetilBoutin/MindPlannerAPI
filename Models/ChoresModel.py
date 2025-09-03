from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from Models import OpenCyclesModel

class Chores(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    context: str | None = Field(default=None)
    lastTime: int | None = Field(default=0)
    frequency: int = Field(default=2) #frequence of the chores in days