# Generated by Django 5.1.5 on 2025-02-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_profile_type_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default=1, max_length=600),
            preserve_default=False,
        ),
    ]
