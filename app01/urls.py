from django.urls import path
from app01.views import index, order

urlpatterns = [
    path("index/", index, name="ind"),
    path("orders/", order, name="ord"),

]
