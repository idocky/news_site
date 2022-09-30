from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'image_show']
    prepopulated_fields = {'slug': ('title',)}

    def image_show(self, obj):
        if obj.picture:
            return mark_safe("<img src='{}' width='120' />".format(obj.picture.url))
        return 'None'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
