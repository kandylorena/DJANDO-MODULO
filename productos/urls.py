from django.urls import path
from . import views
# 2 punto de entrada y aca se manejam todas las rutas (url) de esta aplicacion

urlpatterns = [
    path('', views.home, name='productos'),
    path('login/', views.login, name='pepito'),
    path('register/', views.register, name='pepito'),
    path('dashboard/', views.dashboard, name='pepito'),
    path('venta/', views.venta, name='pepito'),

    path('cervezas/', views.lista_cervezas, name='cervezas'),
]