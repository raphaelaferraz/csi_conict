# Generated by Django 4.0.2 on 2022-08-06 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('titulo_para_url', models.CharField(max_length=45)),
                ('capa', models.ImageField(upload_to='artigos/%Y/%m/%d/')),
                ('data_publicacao', models.DateField(default=datetime.datetime.today)),
                ('tempo_de_leitura', models.IntegerField()),
                ('conteudo', models.TextField()),
                ('resumo', models.TextField()),
                ('referencias', models.TextField()),
                ('tema', models.TextField(choices=[('Seguranca Cibernetica', 'Ciberseg'), ('Seguranca Cibernetica | Crimes Cibernéticos', 'Ciberseg Crimes'), ('Seguranca Cibernetica | LGPD', 'Ciberseg Lgpd')], max_length=45)),
                ('publicado', models.BooleanField(default=False)),
            ],
        ),
    ]