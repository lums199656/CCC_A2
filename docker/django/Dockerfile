FROM python:3.7.2-stretch

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get install -y uwsgi-plugin-python

ENV PYTHONUNBUFFERED 1

RUN mkdir /home
RUN mkdir /home/ubuntu
RUN mkdir /home/ubuntu/A2_

WORKDIR /home/ubuntu/A2_
COPY ../.. .
RUN pip3 install -r ./docker/django/requirements.txt

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8888", "--insecure"]
CMD ["uwsgi", "uwsgi.ini"]