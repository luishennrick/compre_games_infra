from rest_framework import viewsets
from games_infra.models import Produto
from games_infra.serializer import ProdutoSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all().order_by('name')
    serializer_class = ProdutoSerializer


