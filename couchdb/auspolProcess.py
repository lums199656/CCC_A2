# Author: Minshen Lu
# ID : 1039243
# Team : 32

import json


def core():
    INPUT_2014_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2014-processed.json'
    INPUT_2015_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2015-processed.json'
    INPUT_2016_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2016-processed.json'
    INPUT_2017_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2017-processed.json'
    INPUT_2018_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-2018-processed.json'
    OUTPUT_PATH = '/Users/luminshen/Desktop/CCC/twitter-data/twitter-auspol-final.json'
    factor = ["aus_1", "aus_0", "aus_n1", 'aus', "sum_"]
    result = {}
    for year in range(2014, 2019):
        with open(eval('INPUT_' + str(year) + "_PATH")) as file:
            for line in file:
                line = eval(line)['doc']
                if line.get('location') is None:
                    continue
                location = line['location']
                if result.get(location) is None:
                    result[location] = {
                        2014: {"aus_1": 0, "aus_0": 0, "aus_n1": 0, 'aus': 0, "sum_": 0},
                        2015: {"aus_1": 0, "aus_0": 0, "aus_n1": 0, 'aus': 0, "sum_": 0},
                        2016: {"aus_1": 0, "aus_0": 0, "aus_n1": 0, 'aus': 0, "sum_": 0},
                        2017: {"aus_1": 0, "aus_0": 0, "aus_n1": 0, 'aus': 0, "sum_": 0},
                        2018: {"aus_1": 0, "aus_0": 0, "aus_n1": 0, 'aus': 0, "sum_": 0}}
                sen = str(line['sentiments_boolean'])
                if sen == '-1':
                    sen = 'n1'
                result[location][year]['sum_'] += len(line['hashtags'])
                if ('auspol' in line['hashtags']) or ('auspol' + str(year) in line['hashtags']):
                    result[location][year]['aus_' + sen] += 1
                    result[location][year]['aus'] += 1
        print("已完成 {} 年的数据".format(year))

    for key in result:
        for year in range(2014, 2019):
            for sen in range(-1, 2):
                sen_str = str(sen)
                if sen_str == '-1':
                    sen_str = 'n1'
                try:
                    result[key][year]['auspol_' + str(sen) + "_percent"] = int(result[key][year]["aus_" + sen_str] / \
                                                                               result[key][year]["aus"] * 100)
                except ZeroDivisionError:
                    result[key][year]['auspol_' + str(sen) + "_percent"] = 0
            try:
                result[key][year]["auspol_wpercent"] = int(result[key][year]["aus"] / \
                                                           result[key][year]["sum_"] * 10000)
            except ZeroDivisionError:
                result[key][year]["auspol_percent"] = 0

            result[key][year]["auspol"] = int(result[key][year]["aus"])

            for key_ in factor:
                del result[key][year][key_]

    result = json.dumps(result)
    with open(OUTPUT_PATH, 'a') as output_file:
        output_file.write(result)


if __name__ == '__main__':
    core()
