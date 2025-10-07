from django.shortcuts import render

def rest(request):
    return render(request,'rest.html')

def menu(request):
    return render(request, 'menu.html')

def adminis(request):
    return render(request, 'adminis.html')

def contact(request):
    return render(request, 'cont.html')
# Create your views here.
