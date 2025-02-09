# Generated by Django 5.1.5 on 2025-02-07 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_theuser_image_perfil_like_post_like_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.CharField(max_length=300)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.theuser')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='coments',
            field=models.ManyToManyField(blank=True, related_name='Coments', through='User.Coment', to='User.theuser'),
        ),
        migrations.CreateModel(
            name='ComentOfComent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_of_coment', models.CharField(max_length=300)),
                ('coment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.coment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.theuser')),
            ],
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.theuser')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.AddField(
            model_name='post',
            name='saves',
            field=models.ManyToManyField(blank=True, related_name='Saves', through='User.Save', to='User.theuser'),
        ),
    ]
