# Generated by Django 4.0.2 on 2022-03-22 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasygolf', '0004_alter_athlete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default=1987, upload_to='images/'),
            preserve_default=False,
        ),
    ]
