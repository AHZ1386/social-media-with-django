from rest_framework import serializers
from twitter.models import twitt
from Account.models import CustomUser

class TwitteSerializer(serializers.ModelSerializer):
    class Meta:
        model = twitt
        fields = '__all__'


class EditTwitteSerializer(serializers.ModelSerializer):
    class Meta:
        model = twitt
        fields = ('text',)


class PostTwitteSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = twitt
        fields = ('text',)
        

class UserProfileUpdateSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'biography',
                  'last_name', 'first_name', 'username',]
