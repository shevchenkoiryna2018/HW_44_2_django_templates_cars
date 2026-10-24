from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'cars/index.html', context)


def toyota(request):
    context = {}
    return render(request, 'cars/toyota.html', context)


def honda(request):
    context = {}
    return render(request, 'cars/honda.html', context)


def renault(request):
    context = {}
    return render(request, 'cars/renault.html', context)