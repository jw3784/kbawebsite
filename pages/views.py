from django.shortcuts import render
from django.http import HttpResponse
from boardmembers.models import boardmember

def index(request):
    boardmembers = boardmember.objects.all()

    context = {
        'boardmembers': boardmembers
    }
        
    return render(request, 'pages/index.html', context)
    
def about(request):
    boardmembers = boardmember.objects.all()

    context = {
        'boardmembers': boardmembers
    }    
    return render(request, 'pages/about.html', context)

def guidebook(request):
    return render(request, 'pages/guidebook.html')