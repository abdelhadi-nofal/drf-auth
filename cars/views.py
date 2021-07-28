from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Car
from .serializer import CarsSerializer


# Create your views here.

class CarsListView(generics.ListCreateAPIView):
    serializer_class = CarsSerializer
    queryset = Car.objects.all()


class CarDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarsSerializer
    queryset = Car.objects.all()