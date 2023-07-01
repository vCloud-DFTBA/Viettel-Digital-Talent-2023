#Build assets
FROM node:18.16.0-alpine3.17 AS build
WORKDIR /frontend
COPY ./package*.json .
RUN npm i && npm cache clean --force
RUN npm i --save react-bootstrap bootstrap axios redux react-redux redux-thunk redux-logger react-toastify && npm cache clean --force
COPY . .
RUN npm run build

#Serve static assets to NGINX
FROM nginx:1.22.0-alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./* && rm /etc/nginx/conf.d/default.conf
COPY --from=build /frontend/build /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/
CMD ["nginx", "-g", "daemon off;"]