# Generated by Django 2.2 on 2022-10-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20221027_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcategory',
            old_name='cat',
            new_name='cart',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Books', 'Books'), ('Short book', 'Short book'), ('Main book', 'Main book')], max_length=200, null=True),
        ),
    ]
