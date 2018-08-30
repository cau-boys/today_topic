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
        topic['title'] = docu['title']              # 기사 제목
        topic['content'] = docu['content']          # 기사 본문
        topic['content_html'] = docu['pub_html']    # 기사 본문 코드
        topic['url'] = docu['orgUrl']               # 기사 원본 링크
        date = docu['date']                         # 기사 발행일
        date = date[0:4] + '-' + date[4:6] + '-' + date[6:8] + ' ' \
            + date[8:10] + ':' + date[10:12]
        topic['date'] = date

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
