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
        date = docu['date']  # 기사 발행일
        date = date[0:4] + '-' + date[4:6] + '-' + date[6:8] + ' ' \
            + date[8:10] + ':' + date[10:12]

        topic = {
            'title': docu['title'],
            'content': docu['content'],
            'content_html': docu['pub_html'],
            'url': docu['orgUrl'],
            'date': date
        }
        topics.append(topic)

    return topics


# trim topic string
def trim_topics(topics):
    response_data = '인공지능기반 실시간 트랜드 TOP 5\n\n'
    # 먼저 제목리스트를 보여줌
    for topic in topics:
        response_data += topic['title'] + '\n'
        response_data += get_short_url(topic['url']) + '\n\n'

    return response_data


# convert long url to short url
def get_short_url(long_url):
    # json request
    url = 'http://surl.kr/Api/create.php'
    params = {
        'type': 'json',
        'longUrl': long_url
    }
    res = requests.get(url, params=params)

    # convert json to dictionary
    res_data = json.loads(res.text)
    if res_data['status'] == 'success':
        short_url = res_data['shortUrl']
    else:
        short_url = res_data['longUrl']
    print(res_data)
    return short_url


# get an answer of user's question
def get_answer(question):
    accuracy = 0.9  # 90 % accuracy
    category_list = ['entertainment', 'politics', 'economics',
                     'society', 'it', 'world']

    # request topic_list for all categories
    for category in category_list:
        topics = get_topics(30, category)

        # find an answer in topics
        for topic in topics:
            url = 'http://api.datamixi.com/datamixiApi/mrcQa'
            params = {
                'key': '3082028134077943630',
                'paragraph': topic['content'],
                'question': question
            }
            res = requests.get(url, params=params)

            # convert json to dictionary
            result = json.loads(res.text)
            if result['score'] > accuracy:
                return result['answer']
