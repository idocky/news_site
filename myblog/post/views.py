from django.shortcuts import render
from .models import Post

def main_page(request):
    content = {

    }
    return render(request, 'index.html', content)
