# Generated by Django 4.1.9 on 2023-10-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0010_arquivo_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=30, verbose_name='Matricula')),
                ('auntenticacao', models.CharField(max_length=30, verbose_name='Autenticação')),
                ('competencia', models.CharField(max_length=200)),
            ],
        ),
    ]
