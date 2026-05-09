from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, cerveza

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'productos/home.html', {'productos': productos})


def dashboard(request):
    return HttpResponse("dashboard")


def login(request):
    return HttpResponse("login")

def register(request):
    return HttpResponse("register")

def venta(request):
    return HttpResponse("venta")

def lista_cervezas(request):
    cervezas = cerveza.objects.all()
    return render(request, 'beer/beer.html', {'cervezas': cervezas})