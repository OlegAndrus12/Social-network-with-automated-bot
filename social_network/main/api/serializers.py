from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import UserLike

class UserLikeSerializer(serializers.ModelSerializer):
    like_date = serializers.DateField()

    class Meta:
        model = UserLike
        fields = '__all__'

class UserActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "email", "last_login"]