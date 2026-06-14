from django.urls import path
from app1 import views

urlpatterns = [
    path('student/', views.get_student, name='get-student'),
    path('addstudent/', views.add_student, name='add-student'),
    path('student/update/<int:pk>/', views.update_student, name='update-student'),
    path('student/delete/<int:pk>/', views.delete_student, name='delete_student'),
]
