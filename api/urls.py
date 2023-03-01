from django.urls import path
from .views import TwitteList, EditTwitte, PostTwitte, LoginOut, UserProfileUpdate
app_name = 'api'
urlpatterns = [
    path('', TwitteList.as_view(), name='all_twitte_list'),
    path('twitte/edit-twitte/<int:pk>', EditTwitte.as_view(), name='edit_twitte'),
    path('twitte/post-twiite', PostTwitte.as_view(), name='post-twitte'),
    # path('account/followToggle/<str:username>', FollowToggle.as_view(), name='followToggle')
    path("account/logout/", LoginOut.as_view(), name='logout'),
    path("account/update-profile/", UserProfileUpdate.as_view(), name='logout'),
]
