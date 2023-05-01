# NOTE name need to be Dockerfile
FROM python:3.9

RUN python3 -m pip install --upgrade pip
RUN pip3 install flask
RUN pip3 install mysql-connector-python


WORKDIR /app

COPY templates /app/templates
COPY static /app/static
COPY app.py /app

EXPOSE 5000