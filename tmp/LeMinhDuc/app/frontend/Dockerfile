FROM node:18 AS build
WORKDIR /app
COPY ./package* ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.22.0-alpine
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
