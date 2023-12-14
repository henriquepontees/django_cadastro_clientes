from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import date, datetime, timedelta
from apps.app_exemplo.models import Viagens
from apps.app_exemplo.models import Clientes
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def health_check(request):
    """View function for health check"""
    return HttpResponse(status=204)

@method_decorator(login_required, name='dispatch')
class ViagensView(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtendo datas de ontem, hoje e amanhã
        hoje = date.today()
        ontem = hoje - timedelta(days=1)
        amanha = hoje + timedelta(days=1)

        # Buscando viagens de ontem, hoje e amanhã
        passageiros_ontem = Viagens.objects.filter(dataida=ontem) | Viagens.objects.filter(datavolta=ontem)
        passageiros_hoje = Viagens.objects.filter(dataida=hoje) | Viagens.objects.filter(datavolta=hoje)
        passageiros_amanha = Viagens.objects.filter(dataida=amanha) | Viagens.objects.filter(datavolta=amanha)

        # Adicionando os dados ao contexto
        context['passageiros_ontem'] = passageiros_ontem
        context['passageiros_hoje'] = passageiros_hoje
        context['passageiros_amanha'] = passageiros_amanha
        context['hoje'] = hoje
        context['ontem'] = ontem
        context['amanha'] = amanha

        return context
