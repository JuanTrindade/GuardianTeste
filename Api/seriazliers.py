from rest_framework import serializers
from . import models


class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contratos
        fields = '__all__'


class ParcelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parcelas
        fields = '__all__'