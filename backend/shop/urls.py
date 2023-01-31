from django.contrib import admin
from django.urls import path, include
from shop.views import TestView

urlpatterns = [
    path('test/create/', TestView.as_view())
]