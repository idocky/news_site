
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import main_page, add_article, ArticleListView, ArticleDetailView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', ArticleListView.as_view(), name='home'),
    path('new_article/', add_article, name='add_article'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
