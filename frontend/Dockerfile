FROM python:3.10-alpine as builder
WORKDIR /opt/app
COPY . .
RUN pip3 install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
