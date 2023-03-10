from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.showentry, name="showentry"),
    path("result", views.result, name="result"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("random", views.randompage, name="random")
]
