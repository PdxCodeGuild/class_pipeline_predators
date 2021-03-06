# Generated by Django 3.1.4 on 2020-12-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0008_auto_20201230_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='available_authors',
            field=models.CharField(blank=True, choices=[('e.h', 'ERNEST HEMINGWAY'), ('j.d', 'JOAN DIDION'), ('r.b', 'RAY BRADBURY'), ('a.r', 'AYN RAND'), ('g.f', 'GILLIAN FLYNN'), ('j.a', 'JANE AUSTEN')], max_length=200),
        ),
    ]
