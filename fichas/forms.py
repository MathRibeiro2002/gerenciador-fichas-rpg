from django import forms
from django.contrib.auth.models import User # <-- Nova importação
from django.contrib.auth.forms import UserCreationForm # <-- Nova importação
from .models import Ficha

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['nome_personagem', 'template', 'nome_jogo_customizado', 'is_publica']
        
        widgets = {
            'nome_personagem': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #0b132b; color: #fff; border: 1px solid #ffea00;'}),
            'template': forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #0b132b; color: #fff; border: 1px solid #ffea00;'}),
            'nome_jogo_customizado': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #0b132b; color: #fff; border: 1px solid #ffea00;'}),
            'is_publica': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'border: 1px solid #ffea00;'}),
        }
class CadastroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)

    # Aqui nós hackeamos o formulário original para diminuir o limite
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].max_length = 30
        self.fields['username'].help_text = 'Obrigatório. Máximo de 30 caracteres. Letras, números e @/./+/-/_ apenas.'
        self.fields['username'].label = 'Nome de Usuário'        