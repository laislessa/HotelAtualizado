# Generated by Django 4.1 on 2022-09-20 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acomodacoes', '0003_rename_cliete_acomodacao_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoacomodacao',
            name='descricao',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tipoacomodacao',
            name='imagem',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
