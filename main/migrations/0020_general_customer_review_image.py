# Generated by Django 2.2 on 2022-11-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20221104_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='general_customer_review',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
