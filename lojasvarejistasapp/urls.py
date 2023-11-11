from django.urls import path, include
from . import views

urlpatterns = [

    path('cliente/',views.cadastrar_cliente, name='cliente'),

]
