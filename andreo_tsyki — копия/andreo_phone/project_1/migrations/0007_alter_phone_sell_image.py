# Generated by Django 4.1.5 on 2023-03-20 08:36

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('project_1', '0006_alter_phone_sell_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone_sell',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[100, 100], upload_to='for_buy/'),
        ),
    ]
