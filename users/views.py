from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, req=Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
