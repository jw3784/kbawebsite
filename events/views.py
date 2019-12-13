from django.shortcuts import render
from .models import event 

def index(request):
    events = event.objects.all()

    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)
