FROM node:16
WORKDIR /opt/app
COPY ./package.json .
RUN npm install

COPY ./index.js .
CMD node .