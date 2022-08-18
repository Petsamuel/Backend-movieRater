from django.urls import path, include
from rest_framework import routers
from .views import MoviesViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('movie', MoviesViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
