from .models import Cnab
from rest_framework import serializers


class CnabFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = "__all__"
