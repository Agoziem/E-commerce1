# Generated by Django 2.2 on 2022-11-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20221105_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfeatures',
            name='book',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
