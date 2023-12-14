from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models, forms



class IndexView(TemplateView):
    template_name = "app_exemplo/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_examples'] = models.Example.objects.count()
        context['latest_examples'] = models.Example.objects.order_by('-id')[:5]
        return context


class ExampleCreateView(CreateView):
    model = models.Example
    template_name = "app_exemplo/example_create.html"
    form_class = forms.ExampleForm 
    
    def get_success_url(self):
        return reverse_lazy("example:example-detail", kwargs={"pk": self.object.id})
    
    
class ExampleDetailView(DetailView):
    model = models.Example
    template_name = "app_exemplo/example_detail.html"
    context_object_name = "example"

    
class ExampleListView(ListView):
    model = models.Example
    template_name = "app_exemplo/example_list.html"
    context_object_name = "example_list"
    
    
class ExampleListDatatableView(TemplateView):
    model = models.Example
    template_name = "app_exemplo/example_list_datatable.html"
    

class ExampleListJson(BaseDatatableView):
    """
    View para envio de dados para o Datatable
    """
    model = models.Example
    columns = ['id', 'name', 'local', 'timestamp', 'description']  # Adicione aqui os campos que deseja exibir
    order_columns = ['id', 'name', 'local', 'timestamp,' 'description']  # Campos pelos quais será permitido ordenar
    
    def render_column(self, row, column):
        # Esta função permite personalizar a saída dos dados
        return super(ExampleListJson, self).render_column(row, column)


class ExampleUpdateView(UpdateView):
    model = models.Example
    template_name = "app_exemplo/example_update.html"
    form_class = forms.ExampleForm
    
    def get_success_url(self):
        return reverse_lazy("example:example-detail", kwargs={"pk": self.object.pk})


class ExampleDeleteView(DeleteView):
    model = models.Example
    template_name = "app_exemplo/example_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("example:example-list")


@method_decorator(login_required, name='dispatch')
class ClientesCreateView(CreateView):
    model = models.Clientes
    template_name = "app_clientes/clientes_create.html"
    form_class = forms.ClientesForm
    
    def get_success_url(self):
        return reverse_lazy("example:clientes-detail", kwargs={"pk": self.object.id})
    

@method_decorator(login_required, name='dispatch')
class ClientesDetailView(DetailView):
    model = models.Clientes
    template_name = "app_clientes/clientes_detail.html"
    context_object_name = "dados"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.get_object()
        viagens_cliente = models.Viagens.objects.filter(cliente=cliente)
        context['viagens_cliente'] = viagens_cliente
        return context


@method_decorator(login_required, name='dispatch')
class ClientesListView(ListView):
    model = models.Clientes
    template_name = "app_clientes/clientes_list.html"
    context_object_name = "dados"
    

@method_decorator(login_required, name='dispatch')
class ClientesListDatatableView(TemplateView):
    model = models.Clientes
    template_name = "app_clientes/clientes_list_datatable.html"
    

@method_decorator(login_required, name='dispatch')
class ClientesListJson(BaseDatatableView):
    """
    View para envio de dados para o Datatable
    """
    model = models.Clientes
    columns = ['id','nome', 'sobrenome', 'datanascimento', 'passaporte', 'datavalidade']  # Adicione aqui os campos que deseja exibir
    

    def render_column(self, row, column):
        # Esta função permite personalizar a saída dos dados
        return super(ClientesListJson, self).render_column(row, column)


@method_decorator(login_required, name='dispatch')
class ClientesUpdateView(UpdateView):
    model = models.Clientes
    template_name = "app_clientes/clientes_update.html"
    form_class = forms.ClientesForm
    
    def get_success_url(self):
        return reverse_lazy("example:clientes-detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name='dispatch')
class ClientesDeleteView(DeleteView):
    model = models.Clientes
    template_name = "app_clientes/clientes_delete.html"
    context_object_name = "dados"
    
    def get_success_url(self):
        return reverse_lazy("example:clientes-list-datatable")
    

@method_decorator(login_required, name='dispatch')
class ClientesExpiracaoView(TemplateView):
    template_name = "app_clientes/clientes_expiracao_passaportes.html"  # Atualize com o caminho do seu template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.now().date()
        expired_date = today + timedelta(days=180)

        # Filtrando os registros onde a data de validade está expirada ou faltando 180 dias
        expired_clientes = models.Clientes.objects.filter(datavalidade__lte=today)
        expiring_soon_clientes = models.Clientes.objects.filter(datavalidade__lte=expired_date)

        context['expired_clientes'] = expired_clientes
        context['expiring_soon_clientes'] = expiring_soon_clientes

        return context
    
@method_decorator(login_required, name='dispatch')
class ClientesAniversariantesView(TemplateView):
    template_name = "app_clientes/clientes_aniversariantes.html"  # Atualize com o caminho do seu template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.now().date()

        # Filtrando os registros onde o dia e mês de nascimento correspondem ao dia atual
        aniversariantes_do_dia = models.Clientes.objects.filter(
            datanascimento__day=today.day,
            datanascimento__month=today.month
        )

        context['aniversariantes_do_dia'] = aniversariantes_do_dia

        return context
        
    
@method_decorator(login_required, name='dispatch')
class ViagensCreateView(CreateView):
    model = models.Viagens
    fields = ['destino', 'dataida', 'datavolta']
    template_name = 'app_viagens/viagens_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente_id = self.kwargs['cliente_id']
        cliente = get_object_or_404(models.Clientes, pk=cliente_id)
        context['cliente'] = cliente
        return context

    def form_valid(self, form):
        cliente_id = self.kwargs['cliente_id']
        form.instance.cliente_id = cliente_id
        return super().form_valid(form)

    def get_success_url(self):
        cliente_id = self.kwargs['cliente_id']
        return reverse_lazy("example:viagens-list", kwargs={"cliente_id": cliente_id})


@method_decorator(login_required, name='dispatch')
class ViagensDetailView(DetailView):
    model = models.Viagens
    template_name = "app_viagens/viagens_detail.html"
    context_object_name = "viagem"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        viagem = self.get_object()
        context['viagem'] = viagem  # Certifique-se de que 'viagem' contenha o objeto correto
        return context


@method_decorator(login_required, name='dispatch')
class ViagensListView(ListView):
    model = models.Viagens
    template_name = "app_viagens/viagens_list.html"
    context_object_name = "viagens_cliente"  # Renomeie o contexto para refletir uma lista de viagens

    def get_queryset(self):
        cliente_id = self.kwargs.get('cliente_id')  # Obtém o ID do cliente a partir dos parâmetros da URL
        return models.Viagens.objects.filter(cliente_id=cliente_id).order_by('-id')


@method_decorator(login_required, name='dispatch')
class ViagensUpdateView(UpdateView):
    model = models.Viagens
    fields = ['destino', 'dataida', 'datavolta']
    template_name = 'app_viagens/viagens_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        viagem = self.get_object()
        context['viagem'] = viagem
        return context

    def get_success_url(self):
        viagem = self.get_object()
        return reverse_lazy('example:viagens-list', kwargs={'cliente_id': viagem.cliente_id})


@method_decorator(login_required, name='dispatch')
class ViagensDeleteView(DeleteView):
    model = models.Viagens
    template_name = 'app_viagens/viagens_delete.html'
    context_object_name = "dados"

    def get_success_url(self):
        viagem = self.get_object()
        return reverse_lazy('example:viagens-list', kwargs={'cliente_id': viagem.cliente_id})
    
@method_decorator(login_required, name='dispatch')
class ViagensListDatatableView(TemplateView):
    model = models.Viagens
    template_name = "app_viagens/viagens_list_datatable.html"
    

@method_decorator(login_required, name='dispatch')
class ViagensListJson(BaseDatatableView):
    """
    View para envio de dados para o Datatable
    """
    model = models.Viagens
    columns = ['id','destino', 'dataida', 'datavolta']  # Adicione aqui os campos que deseja exibir
    

    def render_column(self, row, column):
        # Esta função permite personalizar a saída dos dados
        return super(ClientesListJson, self).render_column(row, column)