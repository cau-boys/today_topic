from django.http.response import JsonResponse
from today_topic.utils import get_topics


def keyboard(request):
    body = {'key': 'value'}
    return JsonResponse(body)


def messages(request):
    body = {'key': 'value'}
    return JsonResponse(body)
