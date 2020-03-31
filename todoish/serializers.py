from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','preferred name')
        
    def validate_password(self, value: str) -> str:
        return make_password(value)
