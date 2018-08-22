from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('today_topic_api/', include('today_topic.api_urls', namespace='today_topic_api')),
    path('today_topic_site/', include('today_topic.web_urls', namespace='today_topic_site')),
]
