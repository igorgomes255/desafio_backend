from rest_framework import serializers
from .models import Transaction, Cnab


class CnabFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = "__all__"


class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
