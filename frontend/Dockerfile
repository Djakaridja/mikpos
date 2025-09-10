FROM node:20-alpine as base
WORKDIR /usr/src/app
COPY package.json package-lock.json* .npmrc* ./
RUN npm ci || npm i
COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]

