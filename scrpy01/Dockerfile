FROM python:3.12-slim
LABEL authors="andesec"

WORKDIR /app

COPY . /app

RUN pip install flask mysql-connector-python

CMD ["python", "app.py"]
