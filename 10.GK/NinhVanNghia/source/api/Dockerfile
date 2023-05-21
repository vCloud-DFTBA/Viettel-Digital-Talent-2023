FROM node:18-alpine as build

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install -f

COPY . .

RUN npm run build


### Final Stage
FROM node:18-alpine

RUN addgroup --gid 1001 -S vt_app && adduser --uid 1001 -G vt_app -S vt_app

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install --omit=dev -f

RUN chown -R vt_app:vt_app /app

USER vt_app

COPY --from=build /app/dist /app/dist

EXPOSE 8000

CMD ["npm", "start"]
