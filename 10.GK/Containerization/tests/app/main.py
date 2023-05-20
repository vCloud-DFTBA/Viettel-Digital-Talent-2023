from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pymongo


class Attendee(BaseModel):
    id: int
    name: str
    username: str
    birthyear: int
    gender: str
    university: str
    major: str


app = FastAPI()

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["vdt"]


# Get all attendees
@app.get("/vdt-cloud/attendees")
def get_all():
    """
    Get all attendees
    """
    attendees = []
    for item in db["attendees"].find({}, {"_id": 0}):
        item["id"] = int(item["id"])
        attendees.append(item)

    return attendees


# Get a specific attendee by id
@app.get("/vdt-cloud/attendees/{id}")
def get_attendee(id: int):
    """
    Get a specific attendee by id
    """

    # Check id exists or not:
    list_id = [int(item["id"]) for item in db["attendees"].find({})]
    if id not in list_id:
        return {"error": "Attendee not found"}, 404

    attendee = db["attendees"].find_one({"id": id}, {"_id": 0})
    attendee["id"] = int(attendee["id"])
    return attendee


# Add a new attendee
@app.post("/vdt-cloud/attendees")
async def add_attendee(attendee: Attendee):
    """
    Add a new attendee
    """

    # Check id exists or not:
    list_id = [int(item["id"]) for item in db["attendees"].find({})]
    if attendee.id in list_id:
        return {"error": "Id already exists"}, 400

    # Check username exists or not:
    if db["attendees"].find_one({"username": attendee.username}):
        return {"error": "Username already exists"}, 400

    # Add attendee to database:
    db["attendees"].insert_one(dict(attendee))
    return {"message": "Added attendee successfully"}, 201


# Delete an attendee by username
@app.delete("/vdt-cloud/attendees/{username}")
def delete_attendee(username: str):
    # Check username exists or not:
    if db["attendees"].find_one({"username": username}):
        db["attendees"].delete_one({"username": username})
        return {"message": "Deleted attendee successfully"}, 200
    else:
        return {"error": "Username not found"}, 404


# Update an attendee
@app.put("/vdt-cloud/attendees/{username}")
async def update_attendee(username: str, attendee: Attendee):
    """
    Update an attendee
    """

    # Check username exists or not:
    if not db["attendees"].find_one({"username": username}):
        return {"error": "Username not found"}, 404

    # Check new username is unique or not:
    if db["attendees"].find_one({"username": attendee.username}):
        return {"error": "New username already exists"}, 400

    # Check new id is unique or not:
    list_id = [int(item["id"]) for item in db["attendees"].find({})]
    if attendee.id in list_id:
        return {"error": "New id already exists"}, 400

    # Update new attendee to database:
    db["attendees"].update_one({"username": username}, {"$set": dict(attendee)})
    return {"message": "Updated attendee successfully"}, 200


# Update some specific fields of an attendee
@app.patch("/vdt-cloud/attendees/{username}")
async def update_attendee(username: str, attendee: Attendee):
    """
    Update some specific fields of an attendee
    """

    # Check username exists or not:
    if not db["attendees"].find_one({"username": username}):
        return {"error": "Username not found"}, 404

    # Check new username is unique or not (allow duplicate with old username):
    if db["attendees"].find_one({"username": attendee.username}) and username != attendee.username:
        return {"error": "New username already exists"}, 400

    # Check new id is unique or not (allow duplicate with old id):
    list_id = [int(item["id"]) for item in db["attendees"].find({})]
    if attendee.id in list_id and attendee.id != int(db["attendees"].find_one({"username": username})["id"]):
        return {"error": "New id already exists"}, 400

    # Update new attendee to database:
    db["attendees"].update_one({"username": username}, {"$set": dict(attendee)})
    return {"message": "Updated attendee successfully"}, 200


# Show all attendees in a web page
@app.get("/vdt-cloud/web/attendees")
def show_attendees(request: Request):
    """
    Show all attendees in a web page
    """
    attendees = []
    for item in db["attendees"].find({}, {"_id": 0}):
        item["id"] = int(item["id"])
        attendees.append(item)

    # Add order number for each attendee
    for i in range(len(attendees)):
        attendees[i]["order"] = i + 1

    # Set up Jinja2 templates
    templates = Jinja2Templates(directory="templates")

    return templates.TemplateResponse(
        "attendees.html", {"request": request, "attendees": attendees}
    )
