from django.db import models
from django.template.defaultfilters import truncatechars

from django.utils import timezone


class Blog(models.Model):
    """
    Post in DB
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=40, default=' ',
                            help_text='Write the title of the article.')
    preview = models.ImageField(upload_to='posts', default='posts/default.jpg', 
                                help_text='Choose the picture of the article.')
    text = models.TextField(default=' ', help_text='Write the text of the article.')
    created_date = models.DateTimeField(blank=True, default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, default=timezone.now, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def short_text(self):
         return truncatechars(self.text, 50)
         
    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Comment in DB
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    comment_text = models.CharField(max_length=250, default=' ', blank=True)
    published_comment = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.comment_text}'