#FROM php:8.1-apache

#COPY ./app/ /var/www/html/

#RUN docker-php-ext-install mysqli pdo pdo_mysql

FROM python:3.8-alpine
 
COPY ./requirements.txt /app/requirements.txt
 

WORKDIR /app
 

RUN pip install -r requirements.txt
 

COPY ./app/ /app
 

 
CMD ["tail","-f","/dev/null" ]
