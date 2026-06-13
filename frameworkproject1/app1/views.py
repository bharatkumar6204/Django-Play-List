from django.shortcuts import render
from rest_framework.decorators import api_view
from app1.models import Student
from app1.serializes import StudentSerializers
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def list_display(request):
    Students = Student.objects.all()
    serializer = StudentSerializers(Students,many=True)
    return Response(serializer.data)