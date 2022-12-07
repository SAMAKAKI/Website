from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesFrom


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Forma była nie prawidłową'

    form = ArticlesFrom()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
