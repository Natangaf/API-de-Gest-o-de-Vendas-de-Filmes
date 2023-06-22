from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from .serializers import MoviesSerializers,MovieOrderSerializers
from .models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import ItsAdm


class MovieViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ItsAdm]

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all().order_by("id")

        serializer = MoviesSerializers(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = MoviesSerializers(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailsViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ItsAdm]

    def get(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MoviesSerializers(movie)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, req: Request, movie_id: int) -> Response:
        
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrder(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializers(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user ,movie=movie)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)