# Generated by Django 3.2 on 2022-04-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taps', '0009_remove_tap_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='public',
            field=models.BooleanField(default=False, verbose_name='link is public'),
        ),
    ]
