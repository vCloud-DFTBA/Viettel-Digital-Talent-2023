# Create image based on node image
FROM node:19.5.0-alpine as build

WORKDIR /app
ADD . /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm config rm proxy 
RUN npm config rm https-proxy --tried removing npm proxy 
RUN npm install 
RUN npm install react-scripts -g

# Build the app
RUN npm run build

FROM nginx:1.22.0-alpine

COPY --from=build /app/build /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
