from django.contrib import admin
from app1.models import Student

# Register your models here.
class StudenAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','email']
admin.site.register(Student)
