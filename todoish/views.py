from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

# Create your views here.
class ProfileList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = ProfileSerializer(all_users,many=True)
        return Response(serializers.data)
    def post(self, request,format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class EventList(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializers = EventSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save(admin=request.user)
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CreatePostView(APIView):
    permission_classes  = (IsAuthenticated,)
    def get(self,request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            
            serializers.save(user=request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

            