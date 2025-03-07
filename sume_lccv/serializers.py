from rest_framework import serializers

from .models import Projetos, Colaboradores, Financiadores, AreasTecnologicas


class ColaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaboradores
        fields = '__all__'

class FinanciadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiadores   
        fields = ['nome']

class AreasTecnologicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasTecnologicas
        fields = ['nome']


class ProjetosSerializer(serializers.ModelSerializer):
    financiador = serializers.PrimaryKeyRelatedField(
        queryset = Financiadores.objects.all(), many = True)
    
    area_tecnologica = serializers.PrimaryKeyRelatedField(
        queryset = AreasTecnologicas.objects.all(), many = True)
    
    equipe = serializers.PrimaryKeyRelatedField(
        queryset = Colaboradores.objects.all(), many = True)

    class Meta:
        model = Projetos    
        #fields = ['coordenador', 'financiador', 'area_tecnologica', 'ativo', 'equipe']
        fields = '__all__'