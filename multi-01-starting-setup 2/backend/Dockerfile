FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

ENV MONGODB_USERNAME=munnigel
ENV MONGODB_PASSWORD=password

CMD ["npm", "start"]