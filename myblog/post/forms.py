from django import forms
from .models import Category

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, label='Название', widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 7
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all())