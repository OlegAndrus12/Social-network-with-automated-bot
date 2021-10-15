from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserLikeSerializer, UserActivitySerializer
from rest_framework import serializers
from ..models import UserLike
from .utils import validate_datetime
import json



@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "Likes in data range" : 'api/likes'
    }
    return Response(api_urls)


@api_view(['GET'])
def filter_likes_by_date(request):
        if len(request.query_params) == 0:
            likes = UserLike.objects.all()
            serializer = UserLikeSerializer(data = likes, many = True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        start = validate_datetime(request.query_params["date_from"])
        end = validate_datetime(request.query_params["date_to"])
        if not start < end:
            raise serializers.ValidationError({"end_date": "finish must occur after start"})
        else:
            likes = list(UserLike.objects.filter(like_date__range = [start, end]))
            serializer = UserLikeSerializer(data = likes, many = True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    
        return Response({'message': 'Bad Request', 'code' : 400})   


@api_view(['GET'])
def get_user_activity(request):
    users = User.objects.all()
    user_serializer = UserActivitySerializer(data = users, many = True)
    if user_serializer.is_valid():
        user_serializer.save()
    return Response(user_serializer.data)