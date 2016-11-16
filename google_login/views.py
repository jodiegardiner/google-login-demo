from django.shortcuts import render

# Create your views here.


def get_index(request):
    return render(request, 'base.html')


def create(request):
    return render(request, 'formtest.html')
