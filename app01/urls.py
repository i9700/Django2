from django.urls import path
from app01.views import index

urlpatterns = [
    path("index/", index),
]
