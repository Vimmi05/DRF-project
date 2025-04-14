from django.urls import path
from Website import views

urlpatterns = [
    path('', views.Website, name="website"),
    path('CreateTask/', views.CreateTask, name="create_task"),
    path('GetTask/', views.GetTask, name="get_task"),
    path('UpdateTask/<int:id>/', views.UpdateTask, name="update_task"),
    path('Deletetask/<int:id>/', views.DeleteTask, name="delete_task")
]   