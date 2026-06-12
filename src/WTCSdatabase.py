import json
from pymongo import MongoClient

with open("credentials.json") as jsonData:
    creds = json.load(jsonData)
    jsonData.close()
uri = creds["connectionStr"]
client = MongoClient(uri)

def getRaceByID(id):
    database = client.get_database("WTCS")
    try:
        races = database.get_collection("Races")

        # Query for the race
        query = { "_id": id }
        race = races.find_one(query)

        client.close()
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

def getDriverByID(id):
    database = client.get_database("WTCS")
    try:
        drivers = database.get_collection("Drivers")

        query = { "_id": id }
        driver = drivers.find_one(query)

    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

def getRaceByContext(season: int, round: int, session: str):

    database = client.get_database("WTCS")
    try:
        races = database.get_collection("Races")

        if 'q' not in session.lower():
            querySession = "Q"
        elif 's' not in session.lower():
            querySession = "S"
        else:
            querySession = "F"
        query = { "Season": season, "Round": round, "Type": querySession }
        race = races.find_one(query)

        return race
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)