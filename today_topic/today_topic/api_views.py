from django.http.response import JsonResponse
from today_topic.utils import get_topics, trim_topics
from django.views.decorators.csrf import csrf_exempt
import json


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['모든토픽', '엔터테이먼트', '정치', '경제', '사회', 'IT', '세계']
    })


@csrf_exempt # Django에서 Post 방식을 사용했을 때 에러 방지
def message(request):
    # 사용자에게 입력받은 버튼 추출
    request_law = ((request.body).decode('utf-8'))
    request_json = json.loads(request_law)
    subject_kor = request_json['content']

    num_of_topic = 3

    if subject_kor == '모든토픽':
        subject_eng = 'all'
    elif subject_kor == '엔터테이먼트':
        subject_eng = 'entertainment'
    elif subject_kor == '정치':
        subject_eng = 'politics'
    elif subject_kor == '경제':
        subject_eng = 'economics'
    elif subject_kor == '사회':
        subject_eng = 'society'
    elif subject_kor == 'IT':
        subject_eng = 'it'
    elif subject_kor == '세계':
        subject_eng = 'world'
    else :
        subject_eng = 'all'

    topics = get_topics(num_of_topic, subject_eng)
    topics_for_response = trim_topics(topics)

    return JsonResponse({
        'message': {'text': topics_for_response},
        'keyboard': {
            'type': 'buttons',
            'buttons': ['모든토픽', '엔터테이먼트', '정치', '경제', '사회', 'IT', '세계']
        }
    })


