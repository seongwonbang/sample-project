from rest_framework.generics import (
    CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import (
    RegistrationSerializer, LoginSerializer, UserSerializer
)
from .models import (
    User
)


# Create your views here.


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)


'''
serializer save 때매 고생햇다..
perform_create 말고.. save를 할껄..
'''


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']

        return Response({"token": token}, status=status.HTTP_201_CREATED)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
