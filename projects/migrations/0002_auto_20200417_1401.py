# Generated by Django 2.0.2 on 2020-04-17 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='summery',
            new_name='summary',
        ),
    ]
