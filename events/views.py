# LAGT TILL
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
# TAGIT BORT 
#from django.shortcuts import render

# Create your views here.
