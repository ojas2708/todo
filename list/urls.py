from django.contrib import admin
from django.urls import path, include
from list import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path("__reload__/", include("django_browser_reload.urls"))

]
