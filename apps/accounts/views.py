from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions

from .serializers import UserSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]