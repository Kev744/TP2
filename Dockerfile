FROM python:3.7-alpine3.17

ENV API_KEY=$API_KEY
ENV LAT=$LAT
ENV LONGITUDE=$LONG

WORKDIR /app

COPY requirement.txt /app

RUN apk update 
RUN apk upgrade && pip install --no-cache-dir --requirement requirement.txt

COPY apimeteo.py /app

EXPOSE 5000

CMD [ "python", "apimeteo.py" ]