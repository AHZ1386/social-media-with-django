from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from Account.views import UserCreateView, get_current_profile, UserLoginView, edit_profile, LogOutView, get_user, followToggle, search, CustomUserUpdateView, CustomUserDeleteView
from twitter.views import TwitteCreateView, TwitteUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('profile/<str:username>/', get_user, name='get_user'),
    path('profile/', get_current_profile, name='profile'),
    path('edit-profile/', CustomUserUpdateView.as_view(), name='edit_profile'),
    path('singup/', UserCreateView.as_view(), name='singup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('followToggle/<str:user>/', followToggle, name='followToggle'),
    path('edit/<int:pk>', TwitteUpdateView.as_view(), name='edit_twitte'),
    path('find/', search, name='find_user'),
    path('post-twitte/', TwitteCreateView.as_view(), name='add_post'),
    path('delete-account/', CustomUserDeleteView.as_view(), name='delete_account'),
    
    path('api/', include('api.urls'), name='api'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
