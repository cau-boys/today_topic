from django.views.generic.base import TemplateView
from today_topic.utils import get_topics


class IndexView(TemplateView):
    template_name = 'today_topic/index.html'
