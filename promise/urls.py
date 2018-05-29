from django.urls import path
from .views import *

urlpatterns = [
    path('', PromiseListCreateAPIView.as_view()),
    path('<int:pk>', PromiseRetrieveUpdateDestroyAPIView.as_view())
]