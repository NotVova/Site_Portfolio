from django.contrib import admin

from .models import Article, ArticleCategory

admin.site.register(ArticleCategory)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'article', 'images', 'category', 'urls')
    search_fields = ('name',)
