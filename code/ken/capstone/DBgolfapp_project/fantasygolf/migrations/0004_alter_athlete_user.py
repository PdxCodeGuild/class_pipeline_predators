# Generated by Django 4.0.2 on 2022-03-18 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fantasygolf', '0003_delete_player_rename_name_athlete_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
