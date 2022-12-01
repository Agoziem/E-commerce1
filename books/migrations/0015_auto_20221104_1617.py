# Generated by Django 2.2 on 2022-11-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20221103_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ratings',
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=3.5, max_digits=4),
            preserve_default=False,
        ),
    ]
