# Generated by Django 2.2 on 2022-10-30 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20221027_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Hardcopy',
            new_name='Digital',
        ),
    ]
