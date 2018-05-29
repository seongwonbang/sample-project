from rest_framework import serializers
from authentication.models import User
from .models import Article, ArticleLike, Tag


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('slug', 'title', 'description', 'body', 'author', 'tags', 'likes')

    def to_representation(self, obj):
        data = super(ArticleSerializer, self).to_representation(obj)
        data.update({'tags':  obj.tags.values_list('tag', flat=True)})
        return data

    def get_likes(self, obj):
        return obj.articlelike_set.count()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleLikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    article = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, attrs):
        slug = self.context['article_slug']
        try:
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise serializers.ValidationError(
                'article does not exist'
            )
        return {'article': article}

    def create(self, validated_data):
        instance, _ = ArticleLike.objects.get_or_create(
            user=validated_data['user'],
            article=validated_data['article']
        )
        return instance

    class Meta:
        model = ArticleLike
        fields = ('article', 'user')

# class ArticleLikeSerializer(serializers.Serializer):
#     def validate(self, attrs):
#         article_slug = attrs.get('article_slug')
#         user = attrs.get('user')
#         print(attrs)
#         print(article_slug)
#         print(user)
#         article = Article.objects.get(slug=article_slug)
#
#         if not article:
#             raise serializers.ValidationError(
#                 'article does not exist'
#             )
#
#         return {
#             'article': article,
#             'user': user
#         }
#
#     def create(self, validated_data):
#         user = validated_data.get('user')
#         article = validated_data.get('article')
#         article_like, _ = ArticleLike.objects.get_or_create(
#             article=article,
#             user=user
#         )
#         return {
#             'message': 'ok'
#         }
