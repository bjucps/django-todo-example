FROM python:3.8.3

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000