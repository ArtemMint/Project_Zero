from django.contrib import admin
from .models import Profile


class UserAdmin(admin.ModelAdmin):
    model = Profile



admin.site.register(Profile)