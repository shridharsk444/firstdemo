# Generated by Django 3.0.6 on 2020-05-27 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200527_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='adds',
        ),
    ]