# Generated by Django 2.2 on 2022-09-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='order',
            name='ref',
            field=models.CharField(default='none2', max_length=100),
            preserve_default=False,
        ),
    ]
