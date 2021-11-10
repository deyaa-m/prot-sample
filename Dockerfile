From python:3.8-alpine3.11

COPY . /app

WORKDIR /app

RUN make install



