from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('today_topic.api_urls', namespace='api')),
    path('site/', include('today_topic.web_urls', namespace='site')),
]
