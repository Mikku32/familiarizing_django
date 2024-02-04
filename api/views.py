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
            studentList.append({
                'id':i.id,
                'name':i.name,
                'roll':i.roll,
                'course':i.course
                })
        return Response(studentList)
    
    
class StudentDetailApiview(APIView):
    def get(self,request,pk):
        students=Student.objects.get(id=pk)
        return Response({
            'id':students.id,
            'name':students.name,
            'roll':students.roll,
            'course':students.course
            })    
    

            
        
