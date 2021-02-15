from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Realtor

def index(request):
    return render(request, 'realtors/realtors.html')

def realtor(request, realtor_id):
    return render(request, 'realtors/realtor.html')

def search(request):
    return render(request, 'realtors/search.html')
