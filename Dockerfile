FROM python:3.11

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./django-entrypoint.sh /django-entrypoint.sh
RUN chmod +x /django-entrypoint.sh

EXPOSE 8000
