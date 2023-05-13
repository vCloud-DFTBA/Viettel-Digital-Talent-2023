FROM node:18-alpine

RUN addgroup --gid 1001 -S vt_app && adduser --uid 1001 -G vt_app -S vt_app

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN chown -R vt_app:vt_app /app

USER vt_app

RUN npm install --only=prod -f

COPY . .

CMD ["npm", "start"]
