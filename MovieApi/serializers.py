from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Movie, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("id", "username", "password")
        extra_kwargs ={"password":{"write_only":True,"required":True}}
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= ["id", "title", "description", "Stars", "Avg_rating"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields= ["movies", "stars", "user"]