from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, verbose_name='Slug', unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.TimeField(auto_now=True, verbose_name='Дата создания')
    content = models.TextField(verbose_name='Содержание')
    picture = models.ImageField(upload_to='media/postimg', verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
