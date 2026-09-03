from django.db import models
from django.contrib.auth.models import User

# Model 1: Os sistemas ou jogos base disponíveis na plataforma
class TemplateJogo(models.Model):
    nome = models.CharField(max_length=100, help_text="Ex: D&D, Zenless Zone Zero, Customizado")
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

# Model 2: A Ficha em si, pertencente a um usuário
class Ficha(models.Model):
    nome_personagem = models.CharField(max_length=150)
    nome_jogo_customizado = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Preencha se o Template for 'Customizado'"
    )
    
    # Controle de Acesso e Visibilidade
    is_publica = models.BooleanField(default=False, help_text="Marque para expor na plataforma")
    
    # Chaves Estrangeiras Obrigatórias conectando os dados
    template = models.ForeignKey(TemplateJogo, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) 
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_personagem} ({self.autor.username})"

# Model 3: Os campos flexíveis para o usuário colocar qualquer informação
class CampoCustomizado(models.Model):
    nome_do_campo = models.CharField(max_length=100, help_text="Ex: 'Classe', 'Atributo', 'Lore'")
    valor = models.TextField(help_text="Ex: 'Guerreiro', '20', 'História...'")
    
    # Chave Estrangeira ligando o campo à Ficha
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name='campos')

    def __str__(self):
        return f"{self.nome_do_campo} - {self.valor}"
