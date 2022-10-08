from rest_framework import serializers
from .models import Propietario
from .models import Departamento
from .models import Expensa_Agua
from .models import Expensa

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = "__all__"

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = "__all__"

class Expensa_AguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expensa_Agua
        fields = "__all__"

class ExpensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expensa
        fields = "__all__"
