# Generated by Django 3.1 on 2020-08-07 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20200807_0440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='name',
            new_name='title',
        ),
    ]