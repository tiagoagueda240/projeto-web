# Generated by Django 4.0.4 on 2022-05-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_cadeira_anoletivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ano',
            field=models.CharField(choices=[(1, 'ano1'), (2, 'ano2'), (3, 'ano3')], max_length=2),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='semestre',
            field=models.CharField(choices=[(1, 'sem1'), (2, 'sem2')], max_length=2),
        ),
    ]