db = db.getSiblingDB("VDT2023");
db.attendees.drop();

const data = cat("/docker-entrypoint-initdb.d/attendees.json");

db.attendees.insertMany(JSON.parse(data));
