# Generated by Django 4.0.4 on 2022-05-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_lingua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lingua',
            name='nivel',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=5),
        ),
        migrations.AlterField(
            model_name='lingua',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
