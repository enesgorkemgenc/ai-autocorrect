# Generated by Django 4.0.3 on 2022-09-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aiautocorrectapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordrelation',
            old_name='acurate',
            new_name='accurate',
        ),
    ]
