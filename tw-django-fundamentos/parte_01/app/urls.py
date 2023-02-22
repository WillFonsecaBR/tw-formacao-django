from django.urls import path

from .views import form_cliente, horario_atual

urlpatterns = [
    path('horario_atual', horario_atual),
    path('form_cliente', form_cliente),
]
