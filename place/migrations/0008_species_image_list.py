# Generated by Django 3.1 on 2020-08-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_auto_20200809_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='image_list',
            field=models.TextField(blank=True, default=''),
        ),
    ]