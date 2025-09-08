from fastapi import Depends, FastAPI, HTTPException, Query, Response, status
from fastapi.responses import UJSONResponse, RedirectResponse
from typing import Annotated
from Models import DailyJournalingModel, OpenCyclesModel, NextActionsModel, DailyQuestsModel, CallFriendModel, ChoresModel, WishesCyclesModel, ClosedCyclesModel
from sqlmodel import Field, Session, SQLModel, create_engine, select, func
from datetime import datetime, timedelta

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
CONST_URL = "http://127.0.0.1:8000"

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/wishesCycles/")
def create_openCycle(WishesCycles: WishesCyclesModel.WishesCycles, session: SessionDep) -> WishesCyclesModel.WishesCycles:
    session.add(WishesCycles)
    session.commit()
    session.refresh(WishesCycles)
    return WishesCycles


@app.post("/openCycle/")
def create_openCycle(OpenCycles: OpenCyclesModel.OpenCycles, session: SessionDep, response: Response) -> OpenCyclesModel.OpenCycles:
    check = select(func.count(OpenCyclesModel.OpenCycles.id))
    if session.scalar(check) < 10:
        session.add(OpenCycles)
        session.commit()
        session.refresh(OpenCycles)
        return OpenCycles
    response.status_code = status.HTTP_406_NOT_ACCEPTABLE
    response.content = "Too many openCycle try adding to WishesList"
    return response

@app.get("/openCycle/")
def read_openCycles(
    session: SessionDep
) -> list[OpenCyclesModel.OpenCycles]:
    openCycles = session.exec(select(OpenCyclesModel.OpenCycles)).all()
    return openCycles

@app.post("/nextAction/")
def create_nextAction(NextAction: NextActionsModel.NextActions, session: SessionDep) -> NextActionsModel.NextActions:
    session.add(NextAction)
    session.commit()
    session.refresh(NextAction)
    return NextAction

@app.get("/nextAction/")
async def read_nextAction(
    session: SessionDep,
    motivation : int = 10,
) -> list[NextActionsModel.NextActions]:
    print(motivation)
    nextActions = session.exec(select(NextActionsModel.NextActions).where(NextActionsModel.NextActions.done == False).where(NextActionsModel.NextActions.motivation_mini < motivation)).all()
    print(nextActions)
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
    session.refresh(DailyJournaling)
    return DailyJournaling

@app.post("/dailyQuest/")
def write_dailyQuest(DailyQuest: DailyQuestsModel.DailyQuests, session: SessionDep) -> DailyQuestsModel.DailyQuests:
    session.add(DailyQuest)
    session.commit()
    session.refresh(DailyQuest)
    return DailyQuest

@app.get("/dailyQuests/")
def read_dailyQuest(session: SessionDep) -> list[DailyQuestsModel.DailyQuests]:
    quests = session.exec(select(DailyQuestsModel.DailyQuests)).all()
    return quests

@app.get("/callFriend")
def read_callFriend(session: SessionDep) -> list[CallFriendModel.CallFriend]:
    friends = session.exec(select(CallFriendModel.CallFriend)).all()
    return friends

@app.post("/callFriend")
def write_callFriend(CallFriend: CallFriendModel.CallFriend, session: SessionDep) -> CallFriendModel.CallFriend:
    session.add(CallFriend)
    session.commit()
    session.refresh(CallFriend)
    return CallFriend   

@app.get("/allChores/")
def read_chores(session: SessionDep) -> list[ChoresModel.Chores]:
    chores = session.exec(select(ChoresModel.Chores)).all()
    return chores

@app.post("/chores/")
def write_chores(Chore: ChoresModel.Chores, session: SessionDep) -> ChoresModel.Chores:
    session.add(Chore)
    session.commit()
    session.refresh(Chore)
    return Chore

@app.get("/todayChores/")
def get_todaysChores(session: SessionDep) -> list[ChoresModel.Chores]:
    chores = session.exec(select(ChoresModel.Chores).where(ChoresModel.Chores.lastTime > ChoresModel.Chores.frequency)).all()
    print(chores)
    return chores