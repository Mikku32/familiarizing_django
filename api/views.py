from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Student
from api.serializers import StudentSerializer



from rest_framework import generics


# class StudentListApiview(APIView):
#     def get(self,request):
#         students=Student.objects.all() #select * from students
#         studentList=[] #empty list
#         for i in students:
#             studentList.append({
#                 'id':i.id,
#                 'name':i.name,
#                 'roll':i.roll,
#                 'course':i.course
#                 })
#         return Response(studentList)
    

#using serializer example

# class StudentListApiview(APIView):
#     def get(self,request):
#         students=Student.objects.all()
#         stdntserlzr=StudentSerializer(students,many=True)  #many=true because we have multiple students
#         return Response(stdntserlzr.data)



# class StudentDetailApiview(APIView):
#     def get(self,request,pk):
#         students=Student.objects.get(id=pk)
#         return Response({
#             'id':students.id,
#             'name':students.name,
#             'roll':students.roll,
#             'course':students.course
#             })    
    

    #using serializer example

# class StudentDetailApiview(APIView):
#     def get(self,request,pk):
#         stud=Student.objects.get(id=pk)  
#         stdntserlzr=StudentSerializer(stud,many=False)
#         return Response(stdntserlzr.data)          
        



#simple crud operation example

class StudentListApiview(generics.ListCreateAPIView):   #toget(list) and to create (create)
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class StudentDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
