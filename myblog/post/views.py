from django.shortcuts import render
from .models import Post
from .forms import ArticleForm

def main_page(request):
    list_post = Post.objects.all()
    content = {
        'list_post': list_post,

    }
    return render(request, 'index.html', content)

def add_article(request):
    form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})
