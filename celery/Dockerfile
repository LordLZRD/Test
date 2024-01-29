FROM python:3.11

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./celery /usr/src/app/celery
RUN chmod +x /usr/src/app/celery/celery.sh

#ENTRYPOINT ["/bin/bash", "/usr/src/app/celery/celery.sh"]