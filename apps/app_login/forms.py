from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border border-primary', 'placeholder': 'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-primary', 'placeholder': 'Senha'}))
