from django.shortcuts import render
from .models import Article


def get_ingex_page(request):
    articles = Article.objects.all()
    return render(request, 'article/index.html', {'articles': articles})


def get_article_details(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'article/article-details.html', {'article': article})


from django.shortcuts import render

# Create your views here.
