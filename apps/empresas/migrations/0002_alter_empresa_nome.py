# Generated by Django 4.2.2 on 2023-07-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Noe da Empresa'),
        ),
    ]
