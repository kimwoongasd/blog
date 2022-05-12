from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h2>안녕하세요 첫페이지입니다</h2>")