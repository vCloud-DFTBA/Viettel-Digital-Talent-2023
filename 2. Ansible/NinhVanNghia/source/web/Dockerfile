FROM node:18-alpine as build

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install --only=prod -f

COPY . .

RUN npm run build


### Final stage
FROM nginx:1.22.0-alpine

COPY --from=build /app/build /usr/share/nginx/html
