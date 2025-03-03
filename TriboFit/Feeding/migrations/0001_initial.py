# Generated by Django 5.1.5 on 2025-02-28 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=600)),
                ('measure_type', models.CharField(choices=[('G', 'Grama'), ('L', 'Litro')], max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=50)),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=50)),
                ('carbohydrate', models.DecimalField(decimal_places=2, max_digits=50)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=50)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=50)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=50)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=50)),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=50)),
                ('carbohydrate', models.DecimalField(decimal_places=2, max_digits=50)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=50)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=50)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=50)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=50)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Foods', to='Feeding.food')),
            ],
        ),
    ]
