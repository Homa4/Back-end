FROM python:3.13-slim

WORKDIR /app

COPY ./app/requirements.txt .

RUN python3 -m venv venv

ENV PATH="./venv/bin:$PATH"

RUN python -m pip install -r requirements.txt

COPY . /app

CMD ["python3", "./app/main.py"]
