# Generated by Django 4.0.4 on 2022-05-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_alter_projeto_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=50)),
                ('nivel', models.TextField()),
            ],
        ),
    ]
