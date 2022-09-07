from django import forms
from .models import Author, Category

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, label='Название', widget=forms.TextInput())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор')
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 7
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all())