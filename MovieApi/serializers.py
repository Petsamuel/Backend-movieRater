from .models import Movie, Rating
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= ["id", "title", "description"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields= ["movies", "stars", "user"]