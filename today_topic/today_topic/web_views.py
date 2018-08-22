from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'today_topic/index.html'
