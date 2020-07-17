from django.shortcuts import render
from testapp.models import student
# Create your views here.
def homepage_view(request):
    students=student.objects.all()
    return render(request,'testapp/index.html',{'students':students})
