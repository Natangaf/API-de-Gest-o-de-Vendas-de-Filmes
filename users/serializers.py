from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ]
    )
    password = serializers.CharField(max_length=100, write_only=True)
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ],
    )
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(default=False, required=False)
    is_superuser = serializers.BooleanField(required=False, read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):

        if validated_data["password"]:
            new_password = validated_data.pop("password")
            instance.set_password(new_password)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
