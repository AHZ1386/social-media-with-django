from django.shortcuts import render
from rest_framework.generics import ListAPIView
from twitter.models import twitt
from .serializer import TwitteSerializer


class TwitteList(ListAPIView):
    queryset = twitt.objects.all()  
    serializer_class = TwitteSerializer