from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView



# Create your views here.



@api_view
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status': 200, 'payload': serializer.data})


#Generic based Views

from rest_framework import generics

# GET & POST BOTH GENERIC
class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# DELETE AND UPATE BOTH GENERIC

class StudentGeneric1(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'




# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = 


#Class Based Views
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'error': serializer.errors, 'message': 'Something went wrong'})
        serializer.save()
        return Response({'status': 200, 'payload': data, 'message': 'Sent data'})


    def put(self, request):
        try:
            student_objs = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_objs,data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'Something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': request.data, 'message': 'Sent data'})
        
        except Exception as e:
            return Response({'status': 403, 'message': 'You have entered invalid id'})


    def patch(self, request):
        try:
            student_objs = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_objs,data=request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors, 'message': 'Something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': request.data, 'message': 'Sent data'})
        
        except Exception as e:
            return Response({'status': 403, 'message': 'You have entered invalid id'})


    def delete(self, request):
        try:
            student_obj = get_object_or_404(Student, id=id)
            student_obj.delete()
            return Response({'status': 200, 'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'})
        except Exception as e:
            return Response({'status': 500, 'message': 'An error occurred while deleting the student'})
        
    



#Functions based views

# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)
#     return Response({'status': 200, 'payload': serializer.data})


# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status': 403, 'error': serializer.errors, 'message': 'Something went wrong'})
#     serializer.save()
#     return Response({'status': 200, 'payload': data, 'message': 'Sent data'})


# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_objs = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_objs,data=request.data, partial=True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'error': serializer.errors, 'message': 'Something went wrong'})
#         serializer.save()
#         return Response({'status': 200, 'payload': request.data, 'message': 'Sent data'})
    
#     except Exception as e:
#         return Response({'status': 403, 'message': 'You have entered invalid id'})


# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = get_object_or_404(Student, id=id)
#         student_obj.delete()
#         return Response({'status': 200, 'message': 'Student deleted successfully'})
#     except Student.DoesNotExist:
#         return Response({'status': 404, 'message': 'Student not found'})
#     except Exception as e:
#         return Response({'status': 500, 'message': 'An error occurred while deleting the student'})
    



