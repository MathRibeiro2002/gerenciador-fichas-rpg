from django.contrib import admin
from .models import TemplateJogo, Ficha, CampoCustomizado

# Configuração para gabaritar o requisito de Admin Organizado!
@admin.register(TemplateJogo)
class TemplateJogoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ('nome_personagem', 'autor', 'template', 'is_publica')
    list_filter = ('is_publica', 'template') # Adiciona um filtro lateral
    search_fields = ('nome_personagem',)

@admin.register(CampoCustomizado)
class CampoCustomizadoAdmin(admin.ModelAdmin):
    list_display = ('nome_do_campo', 'ficha')
    search_fields = ('nome_do_campo', 'valor')
