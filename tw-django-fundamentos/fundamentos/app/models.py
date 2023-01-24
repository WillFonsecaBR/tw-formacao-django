from django.db import models

""" ACESSO BANCO DE DADOS
BD: tw_django_fundamentos

"""


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=True)
    data_nascimento = models.DateField(null=False, blank=False)
    is_ativo = models.BooleanField(null=False, default=True)
