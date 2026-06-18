from django.shortcuts import render
from app1.models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# CRUD Operation APIView
class StudentAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                student = Student.objects.get(id = pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"errors":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            # read all data
            student = Student.objects.all()
            serializer = StudentSerializer(student,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

