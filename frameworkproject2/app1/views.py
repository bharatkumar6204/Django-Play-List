from django.shortcuts import render
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.serializers import StudentSerializers
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    serializer = StudentSerializers(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"Error":"Student not found"}, status=status.HTTP_404_NOT_FOUND)
    # partial update support
    if request.method=='PATCH':
        serializer = StudentSerializers(student, data=request.data, partial=True)
    else:
        serializer = StudentSerializers(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
