# Generated by Django 4.0.1 on 2022-03-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcmen_dist_app', '0016_remove_article_com_counter_postcomment_com_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='default.jpg', upload_to='images/')),
            ],
            options={
                'ordering': ('picture',),
            },
        ),
    ]
