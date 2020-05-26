# Author: Minshen Lu
# ID : 1039243
# Team : 32

FROM python

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y uwsgi-plugin-python
RUN apt-get install -y python3-pip

ENV PYTHONUNBUFFERED 1

RUN mkdir /home/ubuntu
RUN mkdir /home/ubuntu/A2_
WORKDIR /home/ubuntu/A2_
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8888", "--insecure"]
CMD ["uwsgi", "uwsgi.ini"]