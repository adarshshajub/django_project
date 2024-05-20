from django.urls import path, include
from . import views

app_name = "tree"

urlpatterns = [
    path('', views.home, name="index"),
    path('trees/', views.tree_deatils, name="tree_deatils")
]
