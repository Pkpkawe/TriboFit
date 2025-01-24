# Generated by Django 5.1.5 on 2025-01-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
