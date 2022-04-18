FROM node:17-alpine

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install
RUN npm install react-scripts
RUN npm update react-scripts


COPY . ./

EXPOSE 3000

CMD ["npm", "start"]

