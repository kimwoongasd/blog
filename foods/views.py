from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = str(datetime.now().date())
    context = {'today' : today}
    return render(request, 'foods/index.html', context)

def food_detail(request, food):
    context = dict()
    
    if food == "chicken":
        context["name"] = "뿌랑클"
        context["description"] = "극한의 가성비의 가격"
        context["price"] = 15000
        context["img_path"] = "foods/images/chicken.jpg"
    
    else:
        raise Http404("음식이 없습니다.")
    
    return render(request, 'foods/detail.html', context)