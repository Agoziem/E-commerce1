# Generated by Django 2.2 on 2022-09-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220910_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
