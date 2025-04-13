from django.urls import path
from Home import views

urlpatterns = [
    path('', views.Index ,name="home"),
    path('Home/', views.Home ,name="getStudentApiView"),
    path('CreateStudentsApiView/', views.createStudentApiView, name="createStudent"),
    path('UpdateStudentApiView/<int:id>/', views.updateStudentApiView, name="updateStudent"),
    path('GetStudentApiView/<int:id>/', views.getStudentApiView, name="getStudent"),
    path('DeleteStudentApiView/<int:id>/', views.deleteStudentApiView, name="deleteStudet")
]