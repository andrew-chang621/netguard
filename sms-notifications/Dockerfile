FROM python:3.6.5-alpine3.7

RUN apk update && apk add sudo

COPY requirements.txt template/requirements.txt

RUN pip install -r template/requirements.txt

COPY . /sms-notifications

EXPOSE 300

CMD ["python", "-u", "api.py"]