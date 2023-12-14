from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from . import forms


class CustomLoginView(LoginView):
    template_name = 'app_login/login.html'  # Caminho para o seu template HTML de login
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True  # Redireciona usuários autenticados
    form_class = forms.LoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login:login')  # Redireciona para a página de login após o logout

class CustomRedirectView(RedirectView):
    pattern_name = 'index'  # Redireciona para a página inicial após o login
