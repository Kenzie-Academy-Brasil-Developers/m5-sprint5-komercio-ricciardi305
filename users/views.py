import django
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView, Response, status
from .models import User
from .serializers import UserSerializer, LoginSerializer

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response(
            {"deatail": "invalid email or password"}, status.HTTP_400_BAD_REQUEST
        )


class ListDateJoinedView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
      joined = self.kwargs["num"]
      return self.queryset.order_by("-date_joined")[0:joined]
