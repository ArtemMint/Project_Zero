from django import forms

from .models import Blog, Comment, Category

# choices = [('Nature','Nature'),('Sports','Sports'),('Technology','Technology')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
        choice_list.append(item)

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        labels = {
                'title':'Title:',
                'text':'Text:',
                'preview':'Image to post:',
                'categoty' : 'Category:',
                }
        fields = ('title','category','text','preview')
        widgets = {
                'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
        }
        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        labels = {
                'comment_text':'Comment:',
                }
        fields = ('comment_text',)