from django.urls import path
from app1 import views


urlpatterns = [
    path('student/', views.list_display, name='list_display' )
]

