# Generated by Django 5.0.1 on 2024-01-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_enderecos', '0003_endereco_endereco_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='neighborhood',
            field=models.CharField(blank=True, default='Bairro desconhecido', max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='street',
            field=models.CharField(blank=True, default='Rua Desconhecida', max_length=255, verbose_name='Logradouro'),
        ),
    ]
