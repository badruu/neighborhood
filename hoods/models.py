from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Hoods(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images/', default = 'default.jpg')
    description = models.TextField(max_length = 300, default = 'No description')
    population = models.IntegerField(default = '0')
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def create_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def find_neighbourhood(hoods_id):
        neighbourhood = Hoods.objects.get(id = hoods_id)
        return neighbourhood

    def update_hood(self, item, value):
        self.update(item = value)

    def update_occupants(self, value):
        self.update(population = value)

class Business(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    hood_id = models.ForeignKey(Hoods, on_delete = models.CASCADE)
    email_address = models.EmailField(max_length=254)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(business_id):
        business = Business.objects.get(id = business_id)
        return business

    def update_business(self, item, value):
        self.update(item = value)

    @classmethod
    def search_business(cls, name):
        businesses = cls.objects.filter(name__icontains=name).all()
        return businesses