# Generated by Django 4.0.1 on 2022-01-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_todoitem_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]