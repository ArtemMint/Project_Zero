from django.db import models
from django.utils import timezone


class Blog(models.Model):
    """
    Post in DB
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=40, default=' ')
    preview = models.ImageField(upload_to='posts', default='posts/default.jpg')
    text = models.TextField(default=' ')
    created_date = models.DateTimeField(blank=True, default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, default=timezone.now, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Comment in DB
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    comment_text = models.CharField(max_length=200, default=' ', blank=True)
    published_comment = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.comment_text)
    
