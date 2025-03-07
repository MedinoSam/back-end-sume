# Generated by Django 5.1.6 on 2025-03-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sume_lccv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetos',
            name='area_tecnologica',
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='financiador',
        ),
        migrations.AddField(
            model_name='projetos',
            name='area_tecnologica',
            field=models.ManyToManyField(to='sume_lccv.areastecnologicas'),
        ),
        migrations.AddField(
            model_name='projetos',
            name='financiador',
            field=models.ManyToManyField(to='sume_lccv.financiadores'),
        ),
    ]
