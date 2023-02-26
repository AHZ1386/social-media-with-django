from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from twitter.models import twitt
from .serializer import TwitteSerializer, EditTwitteSerializer
from .permissions import IsAutherOrReadOnly, IsSuperUser

# send all Twitte


class TwitteList(ListCreateAPIView):
    queryset = twitt.objects.all()
    serializer_class = TwitteSerializer
    permission_classes = (IsSuperUser,)

# Edit Twitte


class EditTwitte(RetrieveUpdateAPIView):
    queryset = twitt.objects.all()
    serializer_class = EditTwitteSerializer
    permission_classes = (IsAutherOrReadOnly,)
