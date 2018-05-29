from rest_framework.generics import (
    ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
)
from .serializers import (
    LineSerializer, StationSerializer
)
from .models import (
    Line, Station
)

# Create your views here.

class LineListCreateAPIView(ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class LineRetrieveAPIView(RetrieveAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class StationListCreateAPIView(ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
