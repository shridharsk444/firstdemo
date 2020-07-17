from django.contrib import admin
from testapp.models import student

class studentadmin(admin.ModelAdmin):
    list_display=['rollno','name','dob','marks','email','adds']

admin.site.register(student)