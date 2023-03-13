from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from twitter.models import twitt
from .serializer import TwitteSerializer, EditTwitteSerializer, PostTwitteSerialaizer, UserProfileUpdateSerialaizer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAutherOrReadOnly, IsSuperUser
from rest_framework.views import APIView
from rest_framework.response import Response
from Account.models import CustomUser
from rest_framework.decorators import api_view
from django.contrib.auth import logout
# send all Twitte


class TwitteList(ListAPIView):
    queryset = twitt.objects.all()
    serializer_class = TwitteSerializer
    permission_classes = (IsSuperUser,)

# Edit Twitte


class EditTwitte(RetrieveUpdateAPIView):
    queryset = twitt.objects.all()
    serializer_class = EditTwitteSerializer
    permission_classes = (IsAutherOrReadOnly,)


class PostTwitte(CreateAPIView):
    queryset = twitt.objects.all()
    serializer_class = PostTwitteSerialaizer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(auther=self.request.user)

#################  need to fix ###################


class FollowToggle(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        
        currentUser = CustomUser.objects.get(username=request.user.username)
        user = CustomUser.objects.get(username=username)
        print(currentUser)
        print(user.following.all())
        
        if user in currentUser.following.all():
            currentUser.following.remove(user)
            return Response({"message": "UnFollowed"})
        else:
            currentUser.following.add(user)
            return Response({"message": "Followed"})




class LoginOut(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(200)


class UserProfileUpdate(RetrieveUpdateAPIView):

    queryset = CustomUser.objects.all()

    serializer_class = UserProfileUpdateSerialaizer

    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


@api_view(["get"])
def get_user(request, username):
    user = [
        {
            "user_name": CustomUser.objects.get(username=username).username,
            "first_name": CustomUser.objects.get(username=username).first_name,
            "last_name": CustomUser.objects.get(username=username).last_name,
            "biography": CustomUser.objects.get(username=username).biography,
            "profile_image": CustomUser.objects.get(username=username).profile_image.url,
            "following": CustomUser.objects.get(username=username).following.values('username'),
            "following_number": CustomUser.objects.get(username=username).following.count(),
            "followers": CustomUser.objects.get(username=username).followers.values('username'),
            "followers_number": CustomUser.objects.get(username=username).followers.count(),
            "twittse": CustomUser.objects.get(username=username).twittes.values('text', 'created')
        }

    ]
    return Response(user)
