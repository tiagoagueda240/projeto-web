# Generated by Django 4.0.4 on 2022-05-13 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_autor_alter_post_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='first',
            new_name='apelido',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='last',
            new_name='nome',
        ),
    ]
