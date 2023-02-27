from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.showentry, name="showentry"),
    path("result", views.result, name="result")
]
