from django.forms import ModelForm
from crud.models import Contatos

class ContatosForm(ModelForm):
    class Meta:
        model = Contatos
        fields = ['tipo', 'nome', 'numero']