# Group 32
## Team Members:

* Minshen Lu - 1039243
* Zhe Wang - 1064919
* Zisheng Cheng - 1105176
* Yanming Wang - 1049577
* Kailun Huang - 828808


## Video links

### Ansible

https://youtu.be/RW0KPW1tAsA

### Frontend presentation

https://www.youtube.com/watch?v=tHRdKatbs8s

### PPT

xxx

## Project Structure

### FrontEnd

1. Bootstrap
2. Data visualization
3. Monitor

### BackEnd

Django(8000) -> Nginx reverse proxy port 80 /api
CouchDB related interface
Data query interface
Spider

Apply for the Twitter Developer API
Run the script continuously
Grab data
Data preprocessing
Image preprocessing
Save the image to Object Storage (call backend interface)
Twitter content is stored in the first level of CouchDB (call backend interface)
Natural Language Processing

Model and metrics: Wu-Palmer similarity, NLTK, Profanity, TextBlob
Implement Wu-Palmer similarity on Wordnet to identify the sexual-suggestion message in tweet text
Use Profanity package to identify the violent message in tweet text
Use TextBlob to identify the sentiment of the tweet text
Run the script periodically (once per 30mins)
Grab data from backend
Tokenization of tweet text
Implement three kinds of analytics on each tweet
Upload the result to the second level CouchDB (call backend interface)
Machine Learning

Select model: NSFW, Food Identification
Train model
Run the script periodically (once per 30mins)
Scan the first level CouchDB (call backend interface)
Retrive pictures from the back end
Image Classification
Upload the result to the second level CouchDB (call backend interface)
Deployment Operation

Ansible creates 4 hosts with one click
Docker runs 3 CouchDB instances

## Server Arrangement

Server1: 45.113.234.69
    
    CouchDB/couchdb:lastest
    uwsgi-django/
    Nginx/ nginx:lastest
    cAdvisor/ google/cadvisor:lastest
    spider/


Server2: 115.146.94.169
    
    CouchDB/couchdb:lastest
    uwsgi-django/
    Nginx/ nginx:lastest
    cAdvisor/ google/cadvisor:lastest
    spider/

Server3: 115.146.93.145
    
    CouchDB/couchdb:lastest
    uwsgi-django/
    Nginx/ nginx:lastest
    cAdvisor/ google/cadvisor:lastest
    spider/
    
Server4: 115.146.95.10
    
    CouchDB/couchdb:lastest
    uwsgi-django/
    Grafana/ grafana/grafana:lastest
    InfluxDB/ influxdb:lastest
    cAdvisor/ google/cadvisor:lastest
    
