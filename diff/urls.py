from django.urls import path
from diff.views import *

app_name = 'sep'

urlpatterns = [
    path('sep/', sep, name='sep'),
]