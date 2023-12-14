from django import forms
from . import models


class ExampleForm(forms.ModelForm):
    class Meta:
        model = models.Example
        fields = ["name", "local", "timestamp", "description",]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'timestamp': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ClientesForm(forms.ModelForm):
    class Meta:
        model = models.Clientes
        fields = [ "nome", "sobrenome", "datanascimento", "passaporte", "datavalidade", "contato", "endereco", "cpfcnpj", "email"]
        widgets = {
            
            'nome': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
            'datanascimento': forms.DateInput(attrs={'class': 'form-control border border-primary'}),
            'passaporte': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
            'datavalidade': forms.DateInput(attrs={'class': 'form-control border border-primary'}),
            'contato': forms.NumberInput(attrs={'class': 'form-control border border-primary'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
            'email': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
        }


class ViagemForm(forms.ModelForm):

    class Meta:
        model = models.Viagens
        fields = ['destino', 'dataida', 'datavolta']

        widgets = {
            'destino': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
            'dataida': forms.DateInput(attrs={'class': 'form-control border border-primary'}),
            'datavolta': forms.DateInput(attrs={'class': 'form-control border border-primary'}),
        }
