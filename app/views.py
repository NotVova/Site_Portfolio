from django.shortcuts import render

from .models import Article, ArticleCategory


def home(request):
    context = {
        'title': 'Главная'
    }

    return render(request=request, template_name='portfolio/index.html', context=context)


def projects(request, category_id=None):
    if category_id:
        category = ArticleCategory.objects.get(id=category_id)
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()

    context = {
        'title': 'Проекты',
        'categories': ArticleCategory.objects.all(),
        'articles': articles,
    }

    return render(request=request, template_name='portfolio/projects.html', context=context)
