import datetime
import re
import tweepy
import json as js
import math
import sys

from TweetStore import TweetStore
from textblob import TextBlob

consumer_key = "o0di3qZXxb3u64xSMV7XbKeMx"
consumer_secret = "AAg8S4FtH5fYwgjAwpZnzuyTrbJ80M7txqDZ3EOdOgdW5Ml5gA"
access_token = "1479721442-VdveyqVRtJmC83nPrLf2vHbo2bZBpRlHxaWcZHZ"
access_token_secret = "3UdBzHvXXo1YvVehUkJG7BwYVuSxACd9sBccKlAUZgUza"

COUCH_DATABASE = 'twitter-crawl'

storage = TweetStore(COUCH_DATABASE)


def cal_distance(lat1, lon1, lat2, lon2):
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def get_geodic():
    with open('vic_geo.json') as file:
        data = js.load(file)
        geo_dic = {}
        for line in data['features']:
            ct_name = line['properties']['vic_loca_2']
            coordinates = line['geometry']['coordinates'][0]
            # print('ct_name  :   ', ct_name)
            # print('coordinate  :   ', coordinates)
            avg_la = 0.0
            avg_lo = 0.0
            for coordinate in coordinates:
                avg_la += coordinate[1]
                avg_lo += coordinate[0]
            avg_la = avg_la / len(coordinates)
            avg_lo = avg_lo / len(coordinates)
            # print (avg_la, avg_lo)
            max_dis = 0
            for i in range(len(coordinates)):
                for j in range(len(coordinates)):
                    if i != j:
                        dis = cal_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                        if dis > max_dis:
                            max_dis = dis

            geo_code = 'geocode:"' + str(avg_la) + ',' + str(avg_lo) + ',' + str(max_dis / 2) + 'km"'
            geo_dic[ct_name] = geo_code
    return geo_dic


# storage = TweetStore(COUCH_DATABASE)

def filter_emoji(desstr, restr=''):
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)


def remove_pattern(input_txt):
    match = re.findall(r'@\w+', input_txt)
    match2 = re.findall(r'#\w+', input_txt)
    for i in match:
        input_txt = re.sub(i, '', input_txt)
    for i in match2:
        input_txt = re.sub(i, '', input_txt)

    return input_txt


def remove_symbol(text):
    text_list = re.split('[.!?]', text)
    res = ""
    for t in text_list:
        if len(t) > 10:
            remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
            res = res + re.sub(remove_chars, '', t) + "."
    return res


def space_replace(text):
    return ' '.join(text.split())


def remove_emoji(text):
    text = emoji.demojize(text)
    text = filter_emoji(text, restr='')
    return text


def remove_urls(vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return (vTEXT)


if __name__ == '__main__':
    locate_dic = get_geodic()
    OAUTH_KEYS = {'consumer_key': consumer_key, 'consumer_secret': consumer_secret,
                  'access_token_key': access_token, 'access_token_secret': access_token_secret}
    auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    START_TIME = sys.argv[0]#'2020-04-11'
    print('Crawling...')
    for city_name, geo_code in locate_dic.items():
        try:
            tweets = tweepy.Cursor(api.search,
                                   q=geo_code,
                                   lang='en',
                                   since=START_TIME,
                                   until=datetime.date.today(),
                                   tweet_mode='extended',
                                   count=50000)
        except:
            print("cursor failed")

        for tweet in tweets.items():
            # print(tweet)
            # js_tweet = js.dumps(tweet._json)
            text = tweet.full_text
            text = remove_urls(text)
            text = remove_pattern(text)
            text = text.replace('\n', " ")
            text = remove_symbol(text)
            text = space_replace(text)
            #   print('text :  ', text)
            hash_tag = tweet.entities['hashtags']
            #  print('hashtag :  ', hash_tag)
            time = tweet._json['created_at'].split(" ")
            time = int(time[-1] + month[time[1]] + time[2])
            #   print('time :  ', time)
            id = tweet._json['id_str']
            #   print('time :  ', id)
            blob = TextBlob(text)
            item = {'text': text,
                    'hashtag': hash_tag,
                    'time': time,
                    'id': id,
                    'sentiment': blob.sentiment[0],
                    'location': city_name}
            item = js.dumps(item)
            item = js.loads(item)
            # print (item)
            try:
                if len(hash_tag) != 0:
                    storage.save_tweet(item)
            except:
                print("The data existed!")
        print(city_name, "  round success!")

    print("Crawl finished!")
