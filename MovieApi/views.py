from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes =(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    
    @action(detail=True, methods=["POST"])
    def rate_movie(self, request, pk=None):
        if "stars" in request.data:
            movie = Movie.objects.get(id=pk)
            star = request.data["stars"]
            user = request.user

            try:
                rating =Rating.objects.get(user=user.id, movie=movie.id)
                rating.star=star
                rating.save()
                serializer=RatingSerializer(rating, many=False)
                response={"message":"Rating updated", 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                rating= Rating.objects.create(user=user, movie=movie, star=star)
                serializer=RatingSerializer(rating, many=False)
                response={"message":"Ratings Created", 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response={"message":"you need to provide stars"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
            




class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes =(TokenAuthentication,)
    permission_classes=(IsAuthenticated, )

    def update(self, *args, **kwargs):
        response={"message":"you can't update rating like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def create(self, *args, **kwargs):
        response={"message":"you can't create rating like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
