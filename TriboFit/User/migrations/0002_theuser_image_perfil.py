# Generated by Django 5.1.5 on 2025-02-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theuser',
            name='image_perfil',
            field=models.ImageField(blank=True, default='User/Imagem_Perfil_Vazia.png', upload_to=''),
        ),
    ]
