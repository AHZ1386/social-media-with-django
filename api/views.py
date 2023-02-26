from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView
from twitter.models import twitt
from .serializer import TwitteSerializer, EditTwitteSerializer, PostTwitteSerialaizer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAutherOrReadOnly, IsSuperUser

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
