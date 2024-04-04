from django.shortcuts import render

from django.views.generic import ListView, DetailView
from cafe.models import Menu
# Create your views here.

class MenuLV(ListView) :
    model = Menu

class MenuDV(DetailView) :
    model = Menu