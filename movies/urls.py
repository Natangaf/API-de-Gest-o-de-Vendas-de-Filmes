from django.urls import path
from .views import MovieViews, MovieDetailsViews


urlpatterns = [
    path("movies/", MovieViews.as_view()),
    path("movies/<int:movie_id>/", MovieDetailsViews.as_view()),
]
