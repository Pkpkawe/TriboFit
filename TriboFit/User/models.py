from django.db import models

def TheUser_Directory_Path(instance, filename):
    return f'User/{instance.id}/{filename}'

# Create your models here.

class TheUser(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    telephone = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image_perfil = models.ImageField(null=False, upload_to=TheUser_Directory_Path, default='User/Base/Imagem_Perfil.png')
    following = models.ManyToManyField('self', symmetrical=False, related_name='following')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    friends = models.ManyToManyField('self', related_name='friends')

    def __str__(self):
        return self.name