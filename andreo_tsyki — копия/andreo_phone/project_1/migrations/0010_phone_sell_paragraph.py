# Generated by Django 4.1.5 on 2023-03-24 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_1', '0009_alter_phone_sell_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone_sell',
            name='paragraph',
            field=models.TextField(default=datetime.date.today, verbose_name='paragraph field'),
            preserve_default=False,
        ),
    ]
