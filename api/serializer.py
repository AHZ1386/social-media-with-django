from rest_framework import serializers
from twitter.models import twitt

class TwitteSerializer(serializers.ModelSerializer):
    class Meta:
        model = twitt
        fields = '__all__'