from django.urls import include, path

from .views import ClienteCreateView, ClienteListView

urlpatterns = [
    path("form_cliente", ClienteCreateView.as_view()),
    path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
    
]
