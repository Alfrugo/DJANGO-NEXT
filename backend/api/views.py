from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import PortfolioItem

# def portfolio_list(request):
#     items = PortfolioItem.objects.all()
#     return HttpResponse(items)


def portfolio_list(request):
    items = PortfolioItem.objects.all().values()
    return JsonResponse(list(items), safe=False)


def home(request):
    return HttpResponse("Hello, welcome to my site!")
