import motor.motor_asyncio
import os
from model import Student

# MongoDB driver
mongoHost = os.getenv("MONGODB_HOST", "mongodb")
# url = 'mongodb://mongodb:27017/vdt2023'
url = f'mongodb://{mongoHost}:27017/vdt2023'
client = motor.motor_asyncio.AsyncIOMotorClient(url)

database = client.VDT
collection = database.student


async def fetch_all_students():
    students = []
    cursor = collection.find({})
    async for document in cursor:
        students.append(Student(**document))
    return students
