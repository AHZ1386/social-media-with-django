from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from twitter.models import twitt
from .serializer import TwitteSerializer, EditTwitteSerializer, PostTwitteSerialaizer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAutherOrReadOnly, IsSuperUser
from rest_framework.views import APIView
from rest_framework.response import Response
from Account.models import CustomUser
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
# class FollowToggle(APIView):

#     def get(self, request, username):
#         user = CustomUser.objects.get(username=user)
#         print(user)
#         currentUser = CustomUser.objects.get(username=request.user.username)
#         following = user.following.all()
#         if user == request.user:
#             pass
#         elif user != currentUser.username:
#             if currentUser in following:
#                 user.following.remove(currentUser.id)
#             else:
#                 user.following.add(currentUser.id)

            
        
    
class LoginOut(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(200)