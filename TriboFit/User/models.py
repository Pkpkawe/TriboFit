from django.db import models

# Create your models here.
class TheUser(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    telephone = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome