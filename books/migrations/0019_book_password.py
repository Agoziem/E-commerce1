# Generated by Django 2.2 on 2022-11-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_remove_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Password',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
