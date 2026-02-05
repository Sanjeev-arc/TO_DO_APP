from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("restore-task/<int:id>/", views.restore_task, name="restore_task"),
    path("trash/", views.trash, name="trash"),


]
