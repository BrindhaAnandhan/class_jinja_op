from app1.views import *
from django.urls import path

app_name = 'send'
urlpatterns = [
    path('requests/',requests, name="requests"),
]