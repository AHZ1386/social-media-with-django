from django.urls import path
from .views import TwitteList, EditTwitte, PostTwitte
app_name = 'api'
urlpatterns = [
    path('', TwitteList.as_view(), name='all_twitte_list'),
    path('twitte/edit-twitte/<int:pk>', EditTwitte.as_view(), name='edit_twitte'),
    path('twitte/post-twiite', PostTwitte.as_view(), name='post-twitte'),
]
