# Generated by Django 4.1 on 2022-09-20 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acomodacoes', '0002_cliente_acomodacao_cliete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acomodacao',
            old_name='cliete',
            new_name='cliente',
        ),
    ]
