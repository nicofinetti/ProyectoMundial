# Generated by Django 4.1 on 2022-09-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMundial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partidos',
            name='resutlado',
        ),
        migrations.AddField(
            model_name='partidos',
            name='resultado',
            field=models.CharField(default='por jugar', max_length=50),
            preserve_default=False,
        ),
    ]