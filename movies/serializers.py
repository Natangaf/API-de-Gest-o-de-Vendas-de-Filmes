from rest_framework import serializers
from .models import Movie, CategoryRating, MovieOrder
from users.models import User


class MoviesSerializers(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True,
    )
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, default=None)
    rating = serializers.ChoiceField(
        choices=CategoryRating.choices, default=CategoryRating.G, required=False
    )
    synopsis = serializers.CharField(required=False, default=None)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie


class MovieOrderSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        movie_order = MovieOrder.objects.create(**validated_data)
        return movie_order

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.movie.title
