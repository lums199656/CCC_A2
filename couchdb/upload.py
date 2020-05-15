import json
from uuid import uuid4
import couchdb


def Core():
    IP_ADDRESS = '115.146.95.221'
    DB_NAME = 'twitter-10g'
    FILE_PATH = '/Users/luminshen/Desktop/CCC/twitter-melb.json'

    couch = couchdb.Server('http://admin:admin@{}:5984/'.format(IP_ADDRESS))
    try:
        db = couch.create(DB_NAME)
    except couchdb.http.PreconditionFailed:
        print(DB_NAME, '已存在')

    db = couch[DB_NAME]
    with open(FILE_PATH) as file:
        index_ = 0
        total_row = 0
        datagram = []
        while True:

            # try:
            line = file.readline().rstrip(',\n')
            if index_ == 0:
                total_row = int(line[14:23])
                index_ += 1
                print('0 %')
                continue
            if line == ']}':
                break
            else:
                doc = json.loads(line)
                if 'doc' not in doc:
                    continue
                doc = doc['doc']
                datagram.append(doc)
                if index_ % 10000 == 0:
                    db.update(datagram)
                    datagram = []
                index_ += 1
            if index_ % 100000 == 0:
                print(str(index_ / total_row * 100), "%")
            # except:
            #     print(index_, ' error')
            #     index_ += 1


if __name__ == '__main__':
    Core()
