from django.shortcuts import render
from rest_framework import generics
from .serializers import RRRRSerializer

# Create your views here.
class RRRR(generics.CreateAPIView):
    serializer_class = RRRRSerializer