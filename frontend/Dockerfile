FROM node

WORKDIR /usr/app/frontend
COPY package.json /usr/app/frontend

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]