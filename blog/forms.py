from django import forms

from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        labels = {
                'title':'Title:',
                'text':'Text:',
                'preview':'Image to post:',
                }
        fields = ('title','text','preview')
        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        labels = {
                'comment_text':'Comment:',
                }
        fields = ('comment_text',)