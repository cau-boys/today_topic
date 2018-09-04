from django.views.generic.base import TemplateView
from today_topic.utils import get_topics, find_answer
from django.http import JsonResponse


class IndexView(TemplateView):
    template_name = 'today_topic/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        category = kwargs.get('category')
        if category is not None:
            context['topics'] = get_topics(8, category)
        return context


# get an answer of user's question
def get_answer(request):
    question = request.GET['question']
    answer = find_answer(question)
    return JsonResponse(answer)
