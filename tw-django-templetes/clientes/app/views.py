from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = "lista_clientes"


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_clientes.html"


class ClienteUpdatView(UpdateView):
    model = Cliente
    fields = ("nome", "profissao", "data_aniversario")
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_clientes")


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "lista_cliente.html"
    context_object_name = "cliente"


class ClienteDeletelView(DeleteView):
    model = Cliente
    template_name = "remover_cliente.html"
    success_url = reverse_lazy("lista_clientes")
