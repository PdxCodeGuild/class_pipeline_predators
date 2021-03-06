# Generated by Django 4.0.1 on 2022-01-31 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nick_name', models.CharField(max_length=20)),
                ('phone_num', models.IntegerField()),
                ('schedule', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('nick_name',),
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=15)),
                ('manager', models.CharField(max_length=30)),
                ('brewer', models.CharField(max_length=30)),
                ('delivery', models.CharField(max_length=30)),
                ('notes', models.TextField(max_length=300)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_num', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=10)),
                ('mech_record', models.TextField(max_length=300)),
                ('drivers', models.ManyToManyField(to='mcmen_dist_app.Driver')),
                ('properties', models.ManyToManyField(to='mcmen_dist_app.Property')),
            ],
            options={
                'ordering': ('truck_num',),
            },
        ),
    ]
