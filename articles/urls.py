from django.urls import path
from .views import *

urlpatterns = [
    path('feed', ArticleAPIView.as_view()),
    path('tag', TagAPIView.as_view()),
    path('<article_slug>/like', ArticlesLikeAPIView.as_view())
]