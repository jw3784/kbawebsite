from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import boardmember 


def index(request):
    boardmembers = boardmember.objects.all()
    
    paginator = Paginator(boardmembers, 8)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'boardmembers': paged_listing
    }
    
    return render(request, 'boardmembers/boardmembers.html', context)

