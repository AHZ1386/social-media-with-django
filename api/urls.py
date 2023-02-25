from django.urls import path
from .views import TwitteList
app_name = 'api'
urlpatterns = [
    path('twitte/twitte-list/', TwitteList.as_view(), name='all_twitte_list')
]
