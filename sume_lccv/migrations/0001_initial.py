# Generated by Django 5.1.6 on 2025-03-05 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreasTecnologicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_tecnologica', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Financiadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financiador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordenador', models.CharField(max_length=100)),
                ('ativo', models.BooleanField()),
                ('inicio_vigencia', models.DateField()),
                ('fim_vigencia', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_membros', models.IntegerField()),
                ('area_tecnologica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sume_lccv.areastecnologicas')),
                ('equipe', models.ManyToManyField(to='sume_lccv.colaboradores')),
                ('financiador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sume_lccv.financiadores')),
            ],
        ),
    ]
