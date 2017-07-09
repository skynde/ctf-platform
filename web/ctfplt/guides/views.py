from django.shortcuts import render, get_object_or_404
from .models import Article, Genre

def index(request):
    genres = Genre.objects.all()
    articles = Article.objects.all().order_by("index")
    return render(request,"guides/index.html",
                  {"articles": articles,
                   "genres": genres}
    )

def detail(request, articleTitle):
    article = get_object_or_404(Article, title=articleTitle)
    return render(request,"guides/detail.html",
                  {"article": article,}
    )

