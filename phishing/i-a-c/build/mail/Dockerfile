FROM python:3.8-alpine

WORKDIR /mail

COPY ./mail/ .

RUN pip install mysql-connector-python

CMD ["tail","-f","/dev/null"]
