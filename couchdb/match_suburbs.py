import json

suburbs = open('/Users/luminshen/Documents/代码/PycharmProjects/A2_/couchdb/suburb_list.txt')
suburbs = suburbs.readline().split(',')
set_ = set()
with open('/Users/luminshen/Desktop/CCC/twitter-melb-location.json')as file:
    with open('/Users/luminshen/Desktop/CCC/twitter.json', 'a')as output:
        for index_, line in enumerate(file):
            if index_ % 1000 == 0:
                print('已经处理了 {} 条'.format(index_))

            line = eval(line)
            location = line['doc']['location']
            is_switched = False
            for suburb in suburbs:
                if suburb.startswith(location):
                    print('{} -> {}'.format(location, suburb))
                    line['doc']['location'] = suburb
                    is_switched = True
                    break

            if is_switched is False:
                for suburb in suburbs:
                    if location in suburb:
                        print('{} -> {}'.format(location, suburb))
                        line['doc']['location'] = suburb
                        is_switched = True
                        break
            if is_switched is False:
                print('=====================', location)
            else:
                set_.add(suburb)
            output.write(str(line) + '\n')
        print("获得 {} 个 suburbs 的数据".format(len(set_)))
