from rest_framework import serializers
from .models import Movie, CategoryRating
from users.serializers import UserSerializer


class MoviesSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True,)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False, default=None)
    rating = serializers.ChoiceField(
        choices=CategoryRating.choices, default=CategoryRating.G, required=False
    )
    synopsis = serializers.CharField(required=False, default=None)
    added_by = serializers.CharField(read_only=True ,source="user.email" )

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie
