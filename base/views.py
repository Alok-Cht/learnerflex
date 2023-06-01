from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'lets learn A.I '},
    {'id':3, 'name':'lets learn Machine Learning'},
    {'id':4, 'name':'lets learn Django'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'room.html')
