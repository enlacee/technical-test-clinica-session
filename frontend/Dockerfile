FROM node:18.16.0-alpine

# make the '/usr/app' folder the current working directory
WORKDIR /usr/app

# Available to mount the volumen on container
VOLUME /usr/app

# copy project files and folders to the current working directory (i.e. 'usr/app' folder)
COPY . .

EXPOSE 4000
ENV NODE_ENV=development


