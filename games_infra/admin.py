from django.contrib import admin
from games_infra.models import Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'score', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Produto, Produtos)