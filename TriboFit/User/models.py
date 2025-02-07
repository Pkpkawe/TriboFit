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

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    post = models.FileField(upload_to=TheUser_Directory_Path, null=False, blank=False)
    creator = models.ForeignKey(TheUser, on_delete=models.CASCADE, related_name='Posts', blank=False, null=False)
    likes = models.ManyToManyField(TheUser, related_name='Likes', through='Like', blank=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(TheUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')
    
    def __str__(self):
        return f'{self.user.name} curtiu {self.post.title}'

