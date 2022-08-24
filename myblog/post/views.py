from django.shortcuts import render
from django.views import generic

from .models import Post
from .forms import ArticleForm

def main_page(request):
    content = {

    }
    return render(request, 'index.html', content)

def add_article(request):
    form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

class ArticleListView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'article_list'
    queryset = Post.objects.all()

class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'