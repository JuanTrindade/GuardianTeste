from django.db import models


class Contratos(models.Model):
    data_emissao = models.DateField(
        verbose_name='Data de Emissão',
        blank=False,
        null=False,
    )

    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento do Tomador',
        blank=False,
        null=False,
    )

    valor_desembolsado = models.FloatField(
        verbose_name='Valor Desembolsado',
    )

    cpf = models.FloatField(
        max_length=14,
        null=False,
        blank=False,
    )

    pais = models.CharField(
        null=False,
        blank=False,
        max_length=120,
    )

    estado = models.CharField(
        null=False,
        blank=False,
        max_length=120,
    )

    cidade = models.CharField(
        null=False,
        blank=False,
        max_length=120,
    )

    telefone = models.FloatField(
        verbose_name='Número de Telefone',
        null=False,
        blank=False,
    )

    taxa_contrato = models.FloatField(
        verbose_name='Taxa do Contrato',
        null=False,
        blank=False,
    )

    def __str__(self):
        return {self.cpf}


class Parcelas(models.Model):
    numero_parcela = models.IntegerField(
        verbose_name='Número Atual da Parcela',
        null=False,
        blank=False,
    )

    valor_parcela = models.FloatField(
        verbose_name='Valor Atual da Parcela',
        null=False,
        blank=False,
    )

    data_vencimento = models.DateField(
        verbose_name='Data de Vencimento da Parcela',
        null=False,
        blank=False,
    )

    contrato = models.ForeignKey(
        Contratos,
        verbose_name='ID CONTRATOS',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )