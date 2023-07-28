from .models import Post, Comment
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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
