from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nome', 'preco_por_kg', 'estoque_kg']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nome', 'preco_por_kg', 'quantidade_disponivel']

class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = ['nome_cliente', 'endereco_entrega', 'data_entrega', 'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['metodo_pagamento', 'valor_total']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Item
        fields = ['nome_item', 'quantidade', 'preco_unitario', 'entrega']
