from django.urls import path
from Website import views

urlpatterns = [
    path('', views.Website, name="website"),
    path('GetTask/', views.GetTask, name="get_task")
]