FROM node:18.2.0-alpine
WORKDIR /app
COPY . /app
RUN npm install 
RUN npm run build
CMD ["npm", "start"]