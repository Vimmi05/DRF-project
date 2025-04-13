from django.urls import path
from Blogs import views

urlpatterns = [
    path('', views.CreateBlog, name="create_blogs"),
    path('ReadBlogs/', views.ReadBlog, name="read_blogs"),
    path('DeleteBlog/<int:id>/', views.DeleteBlog, name="delete_blog"),
    path('UpdateBlog/<int:id>/', views.UpdateBlog, name="update_blog"),
    path('ViewBlog/<int:id>/', views.ViewBlog, name="view_blog"),    
]