from django.db import models
from core.models import TimestampedModel


# Create your models here.

class Article(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='articles')
    tags = models.ManyToManyField('articles.Tag', related_name='articles')

    def __str__(self):
        return self.title


class ArticleLike(TimestampedModel):
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("article", "user")


class Comment(TimestampedModel):
    body = models.TextField()

    article = models.ForeignKey(
        'articles.Article', related_name='comments', on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        'authentication.User', related_name='comments', on_delete=models.CASCADE
    )


class CommentLike(TimestampedModel):
    comment = models.ForeignKey('articles.Comment', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)


class Tag(TimestampedModel):
    tag = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.tag
