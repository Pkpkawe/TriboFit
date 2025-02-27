from django.db import models

def TheUser_Directory_Path(instance, filename):
    return f'User/{instance.user.id}/{filename}'

# Create your models here.

class TheUser(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    telephone = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(TheUser, related_name='Profile', on_delete=models.CASCADE)
    image_perfil = models.FileField(null=True, blank=True, upload_to=TheUser_Directory_Path, default='User/Base/Imagem_Perfil.png')
    description = models.CharField(max_length=600, blank=True)
    type_account = models.CharField(max_length=20, choices=(('Normal', 'Normal'), ('Profissional', 'Profissional')), default='Normal')
    following = models.ManyToManyField('self', symmetrical=False, related_name='myfollowings')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='myfollowers')
    friends = models.ManyToManyField('self')
    recommended = models.ManyToManyField('Post.Tag', related_name='RecommendedTags')
