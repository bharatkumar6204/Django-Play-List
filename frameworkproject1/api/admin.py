from django.contrib import admin
from api.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','email']
admin.site.register(Student)
