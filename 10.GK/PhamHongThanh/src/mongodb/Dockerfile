FROM mongo:4.2.24-bionic

ENV MONGO_INITDB_DATABASE=vdt23
# ENV MONGO_INITDB_ROOT_USERNAME=thanh
# ENV MONGO_INITDB_ROOT_PASSWORD=thanh

COPY data.json /data/data.json
COPY ./import-data.sh /docker-entrypoint-initdb.d/
