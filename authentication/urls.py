from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegistrationView.as_view()),
    path('login', LoginView.as_view()),
    path('users', UserListView.as_view()),
    path('users/<int:pk>', UserRetrieveView.as_view())
]