from typing import Annotated
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select
from Models import OpenCyclesModel

class CallFriend(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    friendName: str = Field(default=None)
    lastCall: str = Field(default_factory=datetime.now().strftime("%c"))