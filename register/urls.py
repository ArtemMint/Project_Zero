from django.urls import path
from register.views import sign_in_view, sign_up_view, logout_view

app_name = 'register'
urlpatterns = [
    path('sign_in/', sign_in_view, name='sign_in'),
    path('sign_up/', sign_up_view, name='sign_up'),
    path('logout/', logout_view, name='logout'),
]