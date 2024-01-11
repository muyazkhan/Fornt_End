from django.shortcuts import render
from rest_framework import viewsets
from .models import contactModels
from .seralizer import contact_us

class contuctUsViewSet(viewsets.ModelViewSet):
    queryset = contactModels.objects.all()
    serializer_class = contact_us
# Create your views here.
