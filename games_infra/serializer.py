from rest_framework import serializers
from games_infra.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'name', 'price', 'score', 'image']
