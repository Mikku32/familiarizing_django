from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    


    def post(self,request):
        string1=request.data['message1']
        string2=request.data['message2']
        content = {'message': string1+string2}
        return Response(content)
   
    
class Cars(APIView):
    def get(self,request):
        description={
            
            'car1':{
                'Model':'Suzuki',
                'Color':'Black',
                'Year':'2022',
            },
            'car2':{
                'Model':'Bmw',
                'Color':'White',
                'Year':'2021',

            }
       
        }  
        return Response(description)  
