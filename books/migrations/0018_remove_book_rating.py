# Generated by Django 2.2 on 2022-11-05 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20221105_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
    ]