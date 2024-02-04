from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Student

# Create your views here.

class StudentListApiview(APIView):
    def get(self,request):
        students=Student.objects.all() #select * from students
        studentList=[] #empty list
        for i in students:
            studentList.append({'name':i.name,'roll':i.roll,'course':i.course})
        return Response(studentList)
            
        
