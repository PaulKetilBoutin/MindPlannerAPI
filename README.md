# MindPlannerAPI


# Conception


API todo list

Dailys (Duolinguo, "be more prod", short workout ?) (socle)
Call a friend (Stan, Gaelle, Amandine, Alric ...)
Open Cycles (Scampi)
    Next Actions (A class for the LED 'sensors')
    Waiting Actions (Wating for tarun to send PCB)


Open cycles are long time goals: ex SCAMPI, German learning, Terenor, swimming

Next actions belongs to Open Cycles, very precise
Waitings action are next actions you cannot do yourself

daily quests should be around 30 min tops


One API linked to a sqlite DB (FastAPI / Python) ultimately hosted on a home Raspberry pi
One Terminal client in Python where you can ask what to do today
One React / Material client
Maybe one app ?

Find a way to link motivation levels to tasks

Find a timestamp way to randomize the task I need to takle to keep me on my toes and force me to do managable project


# API

Get All Open Cycles and linked next actions (GET openCycle)
Get All dailys  (GET Dailys)
Add dailys (POST Dailys) // linked or not to a open cycle
Communicate you have done your dailys // (POST dailysDone)
Ask for a task with a mood level (GET nextActions) with a digit on a scale 1 to 10 represneting motivation level
Communicate you have done the task (POST taskDone) with a digit on a scale 1 to 10 representing motivation level, 1 being last small precise task
Add a next action task (POST nextActions) linked to a Open Cycle
Visualise the advancement of open cycle (GET openCycleGrind)
Add Open Cycle with at least 1 next Action (POST open Cycle)


# Schema DB

Open Cycle:
Title: text
EndTimeStamp: date
id: int

NextActions:
id: int
Title: text
Task: text
Motivation: short
OpenCycle: id_OpenCycle
Done: bool
Expected Duration: short // in min

DailyJournaling:
id: int
Comment: text
Date: date
ProudMeter: short

Dailys:
id: int
Title: text
ExpectedDuration: short // in min
OpenCycle: id_OpenCycle (optional)
NumberOfRepetition: int

CallFriend:
id: int
FriendToCall: text
LastCall: date


# Client terminal Python

Be able to ask what to do from the command line of the terminal and to communicate that is is done 
Opportunity to journal the day
auto load a gif and a clock for the beginning of the dailys ?