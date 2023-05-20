db = db.getSiblingDB("test_database");
db.attendees.drop();

const data = cat("/docker-entrypoint-initdb.d/attendees.json");

db.attendees.insertMany(JSON.parse(data));