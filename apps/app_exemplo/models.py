from django.db import models

class Example(models.Model):
    name = models.CharField("Denúncia", max_length=255)
    local = models.CharField("Local", max_length=255)
    timestamp = models.DateTimeField("Data e Hora(formato: (ex.:22/10/2019 12:31:00) )", auto_now_add=False)
    description = models.TextField("Descrição", max_length=400)


    def __str__(self):
        return self.name


class Clientes(models.Model):
    nome = models.CharField("Nome", max_length=255, blank=True, null=True)
    sobrenome = models.CharField("Sobrenome", max_length=255, blank=True, null=True)
    datanascimento = models.DateField("Data de Nascimento", auto_now_add=False, blank=True, null=True )
    passaporte = models.CharField("Passaporte", max_length=255, blank=True, null=True)
    datavalidade = models.DateField("Data de Validade", auto_now_add=False, blank=True, null=True )
    contato = models.PositiveIntegerField("Contato", blank=True, null=True)
    cpfcnpj = models.CharField("CPF ou CNPJ", max_length=400, blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=1000, blank=True, null=True)
    email = models.CharField("Email", max_length=400, blank=True, null=True)


    def __str__(self):
        return self.nome


class Viagens(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    destino = models.CharField("Destino", max_length=255, blank=True, null=True)
    dataida = models.DateField("Data da ida", blank=True, null=True)
    datavolta = models.DateField("Data da Volta", blank=True, null=True)

    def __str__(self):
        return f"Viagem para {self.destino} de {self.cliente.nome}"