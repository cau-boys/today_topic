from django.http.response import JsonResponse


def keyboard(request):
    body = {'key': 'value'}
    return JsonResponse(body)


def messages(request):
    body = {'key': 'value'}
    return JsonResponse(body)
