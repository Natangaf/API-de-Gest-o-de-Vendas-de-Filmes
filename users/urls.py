from django.urls import path
from .views import UserView ,UserViewDetais
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/refresh/", TokenRefreshView.as_view()),
    path("users/<int:user_id>/", UserViewDetais.as_view()),
]
