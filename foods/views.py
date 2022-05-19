from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from foods.models import Menu

# Create your views here.
def index(request):
    context = dict()
    today = str(datetime.now().date())
    menus = Menu.objects.all()
    context['today'] = today
    context['menus'] = menus
    return render(request, 'foods/index.html', context)

def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    
    return render(request, 'foods/detail.html', context)