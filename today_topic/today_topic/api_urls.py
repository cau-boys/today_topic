from django.urls import path
from today_topic import api_views


app_name = 'api'
urlpatterns = [
    path('keyboard/', api_views.keyboard, name='keyboard'),
    path('messages/', api_views.messages, name='messages'),
]
