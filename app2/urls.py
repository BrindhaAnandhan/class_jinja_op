from app2.views import *
from django.urls import path

app_name = 'receive'
urlpatterns = [
    path('response/',response, name="response"),
]