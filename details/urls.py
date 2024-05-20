from django.urls import path
from django.contrib import admin
from . import views 


urlpatterns = [
    # path('admin-author/', views.author_admin, name="author"),
    path("trees/<str:name>", views.tree, name="tree"),
]