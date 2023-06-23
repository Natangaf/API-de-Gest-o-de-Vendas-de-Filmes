from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import itsUser


class UserView(APIView):
    def post(self, req=Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserViewDetais(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, itsUser]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(req, user)

        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(req, user)

        serializer = UserSerializer(instance=user, data=req.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)
