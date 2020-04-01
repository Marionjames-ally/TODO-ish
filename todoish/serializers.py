from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True, default=None)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(),required=False, allow_null=True, default=None)


    class Meta:
        model = Profile
        fields = ('id', 'bio','user','event')

    def validate_password(self, value: str) -> str:
        return make_password(value)

class EventSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), required=False, allow_null=True, default=None)

    class Meta:
        model = Event
        fields = ('id','event','user')

class CategorySerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),required=True, allow_null=True, Default =None)

    class Meta:
        model = Category
        fields = ('event_id', 'event_category')

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), # Or User.objects.filter(active=True)
        required=False, 
        allow_null=True, 
        default=None
    )
    class Meta:
        model = Post
        fields = ('id','post','user','post_created')