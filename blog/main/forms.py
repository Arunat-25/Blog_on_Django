from .models import Post
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'body', 'publish', 'status']
        prepopulated_fields = {'slug': ('title',)}
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'slug': TextInput(attrs={
                'placeholder': 'Слаг'
            }),
            'body': Textarea(attrs={
                'placeholder': 'Текст'
            })
        }