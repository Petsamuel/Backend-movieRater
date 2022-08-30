from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Movie(models.Model):
    title= models.CharField(("Title"), max_length=50)
    description = models.TextField(("Description"),  max_length=360)

    def Stars(self):
        rating = Rating.objects.filter(movies=self)
        return len(rating)

    def Avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(movies=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings)> 0:
            return sum /len(ratings)
        else:
            return 0
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        unique_together = (('user', 'movies'))
        index_together = (('user', 'movies'))

