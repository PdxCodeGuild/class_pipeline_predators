# Generated by Django 4.0.1 on 2022-01-14 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='blog',
            new_name='author',
        ),
    ]
