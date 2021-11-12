from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Type Something....'
        }))

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Type Something....'
        }))

    class Meta:
        model = Comment
        fields = ['comment']
