from django.db import models
from django.urls import reverse

# Representação do banco de dados em forma de classe
class Customer(models.Model):
    # Quando não definimos uma chave primaria o django vai criar um automaticamente.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_city(self):
        return f"{self.city} - {self.state}"

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})
    
    class Meta:
        #Definimos o nome da tabela, se não fizermos isso o django vai criar o nome assim nomeApp_nomeClasse 
        db_table = "customer"