from django.urls import path
from .views import *

urlpatterns = [
    path('lines', LineListCreateAPIView.as_view()),
    path('lines/<pk>', LineRetrieveAPIView.as_view()),
    path('stations', StationListCreateAPIView.as_view()),
    path('stations/<pk>', StationRetrieveUpdateDestroyAPIView.as_view())
]