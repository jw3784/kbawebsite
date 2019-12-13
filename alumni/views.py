from django.shortcuts import render
from rest_framework import viewsets
from .models import alumnus
from .serializers import alumnusSerializer

def index(request):
    alumni = alumnus.objects.all()
    context = {
        'alumni': alumni
    }
    return render(request,'alumni/alumni.html', context)

class alumnusViewSet(viewsets.ModelViewSet):
    queryset = alumnus.objects.all()
    serializer_class = alumnusSerializer