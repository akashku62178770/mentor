from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
import random

# from .helper import MessageHandler
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

# 1
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (IsAuthenticated)
    # authentication_classes = (TokenAuthentication,)

    def testsession(request):
        if request.session.get("test", False):
            print(request.session["test"])
        request.session.set_expiry(1)

        return []


# 2
# class SPViewset(viewsets.ModelViewSet):
#     queryset = StudentProfile.objects.all()
#     serializer_class = StudentProfileSerializer
#     # permission_classes = (IsAuthenticated)
#     # authentication_classes = (TokenAuthentication,)


# class SPViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StudentProfile.objects.all()
#         serializer = StudentProfileSerializer(queryset, many=True)
#         print("list")
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StudentProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = StudentProfile.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         # print(student.usn)
#         print("request.user)")
#         serializer = StudentProfileSerializer(student)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         student = StudentProfile.objects.get(pk=pk)
#         serializer = StudentProfileSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         student = StudentProfile.objects.get(pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 2
class SPViewset(generics.ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     print(request.user)
    #     return super().get_queryset(*args, **kwargs)


# 3
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    print()
    # permission_classes = (IsAuthenticated)
    # authentication_classes = (TokenAuthentication,)


# 4
class PIViewSet(viewsets.ModelViewSet):
    queryset = ParentInteraction.objects.all()
    serializer_class = ParentInteractionSerializer
    # permission_classes = (IsAuthenticated)
    # authentication_classes = (TokenAuthentication,)


# 5
class MGRViewSet(viewsets.ModelViewSet):
    queryset = MentorGeneralRemark.objects.all()
    serializer_class = MentorGeneralRemarkSerializer
    # permission_classes = (IsAuthenticated)
    # authentication_classes = (TokenAuthentication,)


# # 6
# class SAPViewSet(viewsets.ModelViewSet):
#     queryset = StudentAcademicPerformance.objects.all()
#     serializer_class = StudentAcademicPerformanceSerializer
#     # permission_classes = (IsAuthenticated)
#     # authentication_classes = (TokenAuthentication,)


# 7
class SIViewSet(viewsets.ModelViewSet):
    queryset = StudentInteraction.objects.all()
    serializer_class = StudentInteractionSerializer
    # permission_classes = (IsAuthenticated)
    # authentication_classes = (TokenAuthentication,)
