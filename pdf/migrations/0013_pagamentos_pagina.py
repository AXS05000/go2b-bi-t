# Generated by Django 4.1.9 on 2023-10-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0012_pagamentos_arquivo_referencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamentos',
            name='pagina',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
