import json
from uuid import uuid4
import couchdb


def Core():
    IP_ADDRESS = '45.113.234.69'
    # DB_NAME = 'demo_2'
    DB_NAME = 'twitter-2014'
    FILE_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2014-processed.json'

    couch = couchdb.Server('http://admin:admin@{}:5984/'.format(IP_ADDRESS))
    try:
        db = couch.create(DB_NAME)
    except couchdb.http.PreconditionFailed:
        print(DB_NAME, '已存在')

    db = couch[DB_NAME]
    with open(FILE_PATH) as file:
        index_ = 0
        datagram = []
        while True:
            try:
                line = file.readline().rstrip(',\n')
                if len(line) < 10:
                    print('处理结束！')
                    break
                if index_ == 0:
                    print('开始处理...')
                else:
                    line = eval(line)['doc']
                    datagram.append(line)
                    if index_ % 1000 == 0:
                        db.update(datagram)
                        datagram = []
                if index_ % 1000 == 0:
                    print('已经处理了 {} 条'.format(index_))
            except:
                print(index_, ' error')
                print(line)
            index_ += 1


if __name__ == '__main__':
    Core()
