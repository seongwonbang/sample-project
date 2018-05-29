from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
)
from authentication.models import User

from .serializers import (
    PromiseSerializer, UserPromiseSerializer
)
from .models import Promise


# Create your views here.

class PromiseListCreateAPIView(ListCreateAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user1=self.request.user)


class PromiseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer
    permission_classes = (IsAuthenticated, )


class UserPromiseListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPromiseSerializer
    permission_classes = (IsAuthenticated, )


class UserPromiseRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPromiseSerializer
    permission_classes = (IsAuthenticated, )