# Generated by Django 4.0.1 on 2022-02-26 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcmen_dist_app', '0010_rename_lat_property_latx_rename_lng_property_lngx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='latX',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='lngX',
            new_name='longitude',
        ),
    ]