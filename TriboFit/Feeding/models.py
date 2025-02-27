from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.CharField(max_length=600, blank=False, null=False)
    measure_type = models.CharField(max_length=1, choices=(('G', 'Grama'), ('L', 'Litro')), blank=False)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    kcal = models.DecimalField(max_digits=50, decimal_places=2)
    carbohydrate = models.DecimalField(max_digits=50, decimal_places=2)
    protein = models.DecimalField(max_digits=50, decimal_places=2)
    fat = models.DecimalField(max_digits=50, decimal_places=2)
    fiber = models.DecimalField(max_digits=50, decimal_places=2)
    sodium = models.DecimalField(max_digits=50, decimal_places=2)

class Diet(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='Foods', blank=False)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    kcal = models.DecimalField(max_digits=50, decimal_places=2)
    carbohydrate = models.DecimalField(max_digits=50, decimal_places=2)
    protein = models.DecimalField(max_digits=50, decimal_places=2)
    fat = models.DecimalField(max_digits=50, decimal_places=2)
    fiber = models.DecimalField(max_digits=50, decimal_places=2)
    sodium = models.DecimalField(max_digits=50, decimal_places=2)

