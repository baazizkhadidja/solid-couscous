from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   variables = {'nom':'abdrrahmane', 'prenom':'khadidja', 'age': 37, 'nationnality':'Algerienne'}
   return render(request, 'store/index.html', variables)

def detail(request):
    variables = {'shape':'very beautyful'}
    return render(request, 'store/details.html', variables)
