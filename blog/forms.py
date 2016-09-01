from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=100)
    content = forms.CharField(label='content', max_length=300)

    class Meta:
        model = Comment
        fields = ('username', 'content')