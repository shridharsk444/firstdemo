import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')
import django
django.setup()

from testapp.models import student
from faker import Faker
from random import *
fake=Faker()

def phonenum():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1,max=999)
        femail=fake.email()
        #fphonenum=fake.phonenum()
        fadds=fake.address()
        student_record=student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,
                                                      adds=fadds) #phonenumber=fphonenum
populate(30)



