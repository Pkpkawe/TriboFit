# Generated by Django 5.1.5 on 2025-02-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_theuser_image_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theuser',
            name='image_perfil',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
