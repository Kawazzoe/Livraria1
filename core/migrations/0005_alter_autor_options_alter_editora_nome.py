# Generated by Django 4.0.5 on 2022-09-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(max_length=99),
        ),
    ]
