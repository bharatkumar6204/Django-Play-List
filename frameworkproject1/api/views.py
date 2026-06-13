from django.shortcuts import render
from api.models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers

# Create your views here.
@api_view(['GET'])
def get_list(request):
    student = Student.objects.all()
    serializer = StudentSerializers(student, many=True)
    return Response(serializer.data)
