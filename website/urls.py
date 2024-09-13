from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name = 'index'),
    path('email', email_view, name = 'email'),
    path('phone', phone_view, name = 'phone')
    ]

