import json
import requests


# get topic lists
def get_topics(count, category):
    # json request
    url = 'http://api.datamixi.com/datamixiApi/topictoday'
    params = {
        'key': '3082028134077943630',
        'count': count,
        'category': category
    }
    res = requests.get(url, params=params)

    # convert json to dictionary
    res_data = json.loads(res.text)
    docus = res_data['document']

    # get topic list
    topics = list()
    for docu in docus:
        topic = {}
        topic['title'] = docu['title']
        topic['content'] = docu['content']
        topics.append(topic)

    return topics


# trim topic string
def trim_topics(topics):
    response_data = '인공지능기반 실시간 트랜드 TOP 3'
    # 먼저 제목리스트를 보여줌
    for topic in topics:
        response_data + topic['title'] + '\n\n'

    response_data + '————————————————'

    for topic in topics:
        response_data + topic['title'] + '\n\n'
        response_data + topic['content'] + '\n\n'
        response_data + '...............................................................................'

    return response_data
