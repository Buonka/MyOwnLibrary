# Generated by Django 4.0.3 on 2022-03-26 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='type',
            new_name='name',
        ),
    ]