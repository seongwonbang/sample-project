from django.shortcuts import get_object_or_404
from rest_framework import status, serializers, mixins, views
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView, ListCreateAPIView, CreateAPIView, DestroyAPIView
)
from rest_framework.permissions import (
    IsAuthenticated
)

from .serializers import (
    ArticleSerializer, TagSerializer, ArticleLikeSerializer
)

from .models import (
    Article, Tag, ArticleLike
)


# Create your views here.
class ArticleAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated, )


class TagAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


class ArticlesLikeAPIView(mixins.CreateModelMixin, mixins.DestroyModelMixin, views.APIView):
    permission_classes = (IsAuthenticated, )

    def get_serializer_context(self):
        return {'article_slug': self.kwargs['article_slug']}

    def post(self, request, *args, **kwargs):
        article = self.get_article()
        user = self.request.user
        instance, _ = ArticleLike.objects.get_or_create(article=article, user=user)
        return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_article(self):
        slug = self.kwargs['article_slug']
        try:
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise serializers.ValidationError(
                'article does not exist'
            )
        return article

    def get_object(self):
        article = self.get_article()
        user = self.request.user
        instance = get_object_or_404(ArticleLike, user=user, article=article)
        return instance

    # def perform_create(self, serializer):
        # slug = self.kwargs['article_slug']
        # article = Article.objects.get(slug=slug)
        # print(serializers is ArticleLikeSerializer)
        # serializers.save(user=self.request.user, article=article)
        # serializers.save()

    # def post(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     user = request.user
    #     article_slug = kwargs['article_slug']
    #     article = Article.objects.get(slug=article_slug)
    #
    #     if not article:
    #         raise serializers.ValidationError(
    #             'article does not exist'
    #         )
    #
    #     article_like, created = ArticleLike.objects.get_or_create(
    #         article=article,
    #         user=user
    #     )
    #
    #     if not created:
    #         raise serializers.ValidationError(
    #             'already liked'
    #         )
    #
    #     return Response({"response": 'ok'}, status=status.HTTP_201_CREATED)
