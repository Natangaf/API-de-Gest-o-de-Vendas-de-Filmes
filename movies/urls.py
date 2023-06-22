from django.urls import path
from .views import MovieViews, MovieDetailsViews, MovieOrder


urlpatterns = [
    path("movies/", MovieViews.as_view()),
    path("movies/<int:movie_id>/", MovieDetailsViews.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrder.as_view()),
]
