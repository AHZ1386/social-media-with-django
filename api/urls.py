from django.urls import path
from .views import TwitteList,EditTwitte
app_name = 'api'
urlpatterns = [
    path('', TwitteList.as_view(), name='all_twitte_list'),
    path('twitte/twitte-edit/<int:pk>', EditTwitte.as_view(), name='edit_twitte'),
]
