from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ['content']
        widgets = {
            forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your comment...'       
            })
        }