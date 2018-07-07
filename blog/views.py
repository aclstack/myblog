from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    article = models.Article.objects.get(pk=2)
    return render(request, 'blog/index.html', {'article': article})
