# Generated by Django 4.0.4 on 2022-05-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_alter_cadeira_topicosabordados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologia',
            name='acronimo',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
