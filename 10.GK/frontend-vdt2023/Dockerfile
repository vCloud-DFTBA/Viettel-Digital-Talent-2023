# Stage 1: Build
FROM node:14-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build

# Stage 2: Runtime
FROM node:14-alpine
WORKDIR /app
COPY --from=build-stage /app /app
CMD ["npm", "start"]