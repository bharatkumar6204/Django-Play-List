from rest_framework import serializers
from app1.models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # to include all fields