CREATE TABLE OpenCycle(
    openCycle_id INTEGER PRIMARY KEY
    title TEXT NOT NULL
    endTimeStamp DATE NOT NULL
);

CREATE TABLE NextActions(
    nextActions_id INTEGER PRIMARY KEY
    title TEXT NOT NULL
    task TEXT NOT NULL
    motivation_min INTEGER NOT NULL
    openCycle_id INTEGER FOREIGN KEY
    done BOOLEAN DEFAULT FALSE
    expectedDuration INTEGER NOT NULL
    realDuration INTEGER DEFAULT 0);

CREATE TABLE DailyJournaling(
    dayliJournaling_id INTEGER PRIMARY KEY
    comment TEXT NOT NULL
    journalingDate DATE DEFAULT TODAY
    proudMeter SHORT NOT NULL);

CREATE TABLE DailyQuests(
    dayli_id INTEGER PRIMARY KEY
    title TEXT NOT NULL
    expectedDuration INTEGER NOT NULL
    openCycle_id INTEGER OPTIONAL
    numberOfRepetitions INTEGER NOT NULL DEFAULT 0);

CREATE TABLE CallFriend(
    friend_id INTEGER PRIMARY KEY
    friendName TEXT NOT NULL
    lastCall DATE NOT NULL);
