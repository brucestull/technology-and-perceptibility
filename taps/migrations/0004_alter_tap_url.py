# Generated by Django 3.2 on 2022-04-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taps', '0003_tap_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tap',
            name='url',
            field=models.URLField(blank=True, help_text='url of page which has content of interest for accessiblity'),
        ),
    ]
