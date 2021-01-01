from django.urls import path
from blog.views import home_view, blog_view, blog_detail_view, new_post_view

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('blog/', blog_view, name='blog'),
    path('blog/<int:blog_id>/', blog_detail_view, name='blog_detail'),
    path('blog/new_post/', new_post_view, name='new_post'),
]