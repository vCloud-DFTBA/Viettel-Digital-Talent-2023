import motor.motor_asyncio
from model import Student

# MongoDB driver
# url = 'mongodb://localhost:27017'
url = 'mongodb://host.docker.internal:27017'
client = motor.motor_asyncio.AsyncIOMotorClient(url)

database = client.VDT
collection = database.student


async def fetch_all_students():
    students = []
    cursor = collection.find({})
    async for document in cursor:
        students.append(Student(**document))
    return students
