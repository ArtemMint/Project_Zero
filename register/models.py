from django.db import models

# Create your models here.
class User(models.Model):
    """
    User in DB
    """
    username = models.CharField(max_length=120, blank=False, unique=True)
    email = models.EmailField(max_length=150, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    # picture = models.ImageField(upload_to='users', blank=True)
    # first_name = models.CharField(max_length=50, blank=True)
    # last_name = models.CharField(max_length=50, blank=True)
    # phone_number = models.CharField(max_length=15, blank=True)
    # country = models.CharField(max_length=100, blank=True)
    # address = models.CharField(max_length=100, blank=True)     
    
    def __str__(self):
        return self.username