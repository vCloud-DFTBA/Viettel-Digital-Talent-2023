FROM mongo:5.0 

COPY attendees.json /docker-entrypoint-initdb.d/attendees.json

COPY init-db.js /docker-entrypoint-initdb.d/init-db.js

CMD ["mongod", "--bind_ip_all"]
