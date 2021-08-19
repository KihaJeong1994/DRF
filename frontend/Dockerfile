FROM node

WORKDIR /usr/app/frontend

ENV PATH /usr/app/frontend/node_modules/.bin:$PATH

COPY package.json /usr/app/frontend

RUN npm install

EXPOSE 3000
CMD ["npm", "start"]