FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y gcc python3-dev && \
    pip3 install .

ENTRYPOINT python3 -m chat_home_automation