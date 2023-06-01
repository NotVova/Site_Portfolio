from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категоря'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=128)
    article = models.TextField()
    images = models.ImageField(upload_to='static/img/article_imgs')
    urls = models.URLField(null=True, blank=True)
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
