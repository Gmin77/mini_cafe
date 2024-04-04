from django.urls import path
from . import views
from cafe.views import MenuLV, MenuDV

urlpatterns = [
    path('Menu/', MenuLV.as_view(), name='index'),
    path('Menu/<int:pk>/', MenuDV.as_view(), name='detail'),
]