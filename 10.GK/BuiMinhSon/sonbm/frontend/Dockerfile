FROM node:18.16.0-alpine3.17 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install axios
COPY . .
RUN npm run build

FROM nginx:1.22.0-alpine AS production
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]