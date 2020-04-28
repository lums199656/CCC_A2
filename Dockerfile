FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/A2_
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8888
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8888", "--insecure"]
CMD ["uwsgi", "—-ini", "uwsgi.ini", "&"]