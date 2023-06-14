from fastapi import APIRouter
from models.attendee_model import Attendee
from config.database import collection_name
from schemas.attendee_schema import serializeList, serializeDict

attendee_API = APIRouter()

# Get attendees list
@attendee_API.get("/")
async def get_attendee_list():
    attendee = serializeList(collection_name.find({},{'_id': False}))
    return attendee

# Get attendee info with username
@attendee_API.get("/{username}")
async def get_attendee(username: str):
    return serializeDict(collection_name.find_one({"username": username}, {'_id': False}))


# Add attendee
@attendee_API.post("/newAttendee={username}")
async def add_attendee(attendee: Attendee):
    _id = collection_name.insert_one(dict(attendee))
    return {
        "message": "Add new attendee successfully",
        "data": serializeList(collection_name.find({"_id": _id.inserted_id}, {'_id': False}))
    }


# Edit attendee's info
@attendee_API.put("/editAttendee={username}")
async def update_attendee(username: str, attendee: Attendee):
    collection_name.find_one_and_update({"username": username}, {
        "$set": dict(attendee)
    })
    return {
        "message": "Update attendee successfully",
        "data": serializeDict(collection_name.find({"username": username}))
    }

# Delete attendee
@attendee_API.delete("/deleteAttendee={username}")
async def delete_attendee(username: str):
    collection_name.find_one_and_delete({"username": username})
    return {"message": "Delete attendee successfully"}