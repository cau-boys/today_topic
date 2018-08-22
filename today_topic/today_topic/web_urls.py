from django.urls import path
from today_topic import web_views


app_name = 'today_topic'
urlpatterns = [
    path('', web_views.IndexView.as_view(), name='index'),
]