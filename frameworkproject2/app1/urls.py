from django.urls import path
from app1 import views

urlpatterns = [
    path('student/', views.get_student, name='get-student'),
]
