from fastapi import Depends, FastAPI, HTTPException, Query
from typing import Annotated
from Models import DailyJournalingModel, OpenCyclesModel, NextActionsModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/openCycle/")
def create_openCycle(OpenCycles: OpenCyclesModel.OpenCycles, session: SessionDep) -> OpenCyclesModel.OpenCycles:
    session.add(OpenCycles)
    session.commit()
    session.refresh(OpenCycles)
    return OpenCycles

@app.get("/openCycle/")
def read_openCycles(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[OpenCyclesModel.OpenCycles]:
    openCycles = session.exec(select(OpenCyclesModel.OpenCycles).offset(offset).limit(limit)).all()
    return openCycles

@app.post("/nextAction/")
def create_nextAction(NextAction: NextActionsModel.NextActions, session: SessionDep) -> NextActionsModel.NextActions:
    session.add(NextAction)
    session.commit()
    session.refresh(NextAction)
    return NextAction

@app.get("/nextAction/")
def read_nextAction(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[NextActionsModel.NextActions]:
    nextActions = session.exec(select(NextActionsModel.NextActions).offset(offset).limit(limit)).all()
    return nextActions

@app.get("/nextAction/{openCyleId}")
def read_nextAction(
    session: SessionDep,
    openCycleId: int,
) -> list[NextActionsModel.NextActions]:
    nextAction = session.exec(select(NextActionsModel.NextActions).where(NextActionsModel.NextActions.openCycle_id == openCycleId))
    return nextAction

@app.get("/journalingArhives/")
def read_journal(
    session: SessionDep
)-> list[DailyJournalingModel.DailyJournaling]:
    journaling = session.exec(select(DailyJournalingModel.DailyJournaling)).all()
    return journaling

@app.post("/dailyJournaling/")
def write_journal(DailyJournaling: DailyJournalingModel.DailyJournaling, session: SessionDep) -> DailyJournalingModel.DailyJournaling:
    session.add(DailyJournaling)
    session.commit()
    session.refresh()
    return DailyJournaling