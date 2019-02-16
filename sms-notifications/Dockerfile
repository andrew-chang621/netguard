FROM python:3.6.5-alpine3.7

RUN apk update && apk add sudo

WORKDIR /sms-notifications

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 5000

CMD ["python", "-u", "app.py"]