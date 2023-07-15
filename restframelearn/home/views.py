from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *;
from .serializers import *
from rest_framework.views import  APIView
from rest_framework import generics
# Create your views here.


@api_view(['GET'])
def get_book(request):
    book_obj = book.objects.all()
    serializer = BookSerializer(book_obj,many=True)
    return Response({'status':200, 'payload': serializer.data})

class StudentList(generics.ListCreateAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class Studentdeleteupdate(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "id"  

# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated 
# class StudentAPI(APIView):
#     authentication_classes =[ JWTAuthentication ]
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
        
#         student_obj = Student.objects.all()
#         serializer = StudentSerializer(student_obj,many=True)
#         return Response({'status':200, 'payload': serializer.data})
    
#     def post(self,request):
#         #print(data)
#         serializer = StudentSerializer(data = request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'something went wrong'})
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'messge' : 'okay, saved'})
    
#     def put(self,request):
#         #data = request.data
#         #print(data)
        
#         try:
#             student_obj = Student.objects.get(id = request.data['id'])
#             serializer = StudentSerializer(student_obj, data = request.data)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'something went wrong'})
#             serializer.save()


#             return Response({'status': 200, 'payload': serializer.data, 'messge' : 'okay, saved'})
#         except Exception as e:
#             print(e)

#             return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'invalid id'})
        
#     def patch(self,request):
#         #data = request.data
#         #print(data)
        
#         try:
#             student_obj = Student.objects.get(id = request.data['id'])
#             serializer = StudentSerializer(student_obj, data = request.data, partial = True)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'something went wrong'})
#             serializer.save()


#             return Response({'status': 200, 'payload': serializer.data, 'messge' : 'okay, saved'})
#         except Exception as e:
#             print(e)

#             return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'invalid id'})
        
#     def delete(self,request):
#         try:

#             Student_obj = Student.objects.get(id =request.data['id'])
#             Student_obj.delete()
#             return Response({'status': 200, 'messge' : 'deleted'})
#         except Exception as e:
#             print(e)
#         return Response({'status': 403 , 'messge' : 'invalid id'})





# @api_view(['GET'])
# def home(request):
#     student_obj = Student.objects.all()
#     serializer = StudentSerializer(student_obj,many=True)

#     return Response({'status':200, 'payload': serializer.data})

# @api_view(['POST'])
# def poststudent(request):
#     #print(data)
#     serializer = StudentSerializer(data = request.data)
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'something went wrong'})
#     serializer.save()


#     return Response({'status': 200, 'payload': serializer.data, 'messge' : 'okay, saved'})

# @api_view(['PATCH'])
# def update_student(request,id):
#     data = request.data
#     #print(data)
#     try:
#         student_obj = Student.objects.get(id = id)

#         serializer = StudentSerializer(student_obj, data = request.data, partial = True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'something went wrong'})
#         serializer.save()


#         return Response({'status': 200, 'payload': serializer.data, 'messge' : 'okay, saved'})
#     except Exception as e:
#         print(e)
#         return Response({'status': 403,'errors' : serializer.errors, 'messge' : 'invalid id'})
    
# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:

#         Student_obj = Student.objects.get(id = id)
#         Student_obj.delete()
#         return Response({'status': 200, 'messge' : 'deleted'})
#     except Exception as e:
#         print(e)
#         return Response({'status': 403 , 'messge' : 'invalid id'})
