from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'idade', "data_nascimento", 'is_ativo')
