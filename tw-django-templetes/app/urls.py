from django.urls import path

from .views import (ClienteCreateView, ClienteDeletelView, ClienteDetailView,
                    ClienteListView, ClienteUpdatView)

urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view()),
    path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
    path("form_clientes/<int:pk>", ClienteUpdatView.as_view(), name="editar_cliente"),
    path("lista_cliente/<int:pk>", ClienteDetailView.as_view(), name="listar_clientes"),
    path("delete_cliente/<int:pk>", ClienteDeletelView.as_view(), name="delete_cliente"),
]
