from django.db import models


class CnabType(models.Choices):
    Debito = 1
    Boleto = 2
    Financiamento = 3
    Crédito = 4
    Recebimento_Empréstimo = 5
    Vendas = 6
    Recebimento_TED = 7
    Recebimento_DOC = 8
    Aluguel = 9


class Transaction(models.Model):
    type = models.IntegerField(choices=CnabType.choices)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.TextField(max_length=11)
    card = models.TextField(max_length=12)
    hour = models.TimeField()
    owner_shop = models.TextField(max_length=14)
    name_shop = models.TextField(max_length=19)
