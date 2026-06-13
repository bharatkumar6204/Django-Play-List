from django.shortcuts import render
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.serializers import StudentSerializers

# Create your views here.
@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data)