# Generated by Django 2.2 on 2022-10-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20221030_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='long_description',
        ),
        migrations.AddField(
            model_name='book',
            name='short_description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
