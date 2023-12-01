from rest_framework import serializers
from .models import Vehiculo, VehiculoDocumento

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class VehiculoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoDocumento
        fields = '__all__'
