from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = "lista_clientes"


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_clientes.html"
