# Generated by Django 3.2 on 2022-04-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taps', '0006_tap_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tap',
            name='description',
            field=models.TextField(help_text='\n            extended description of what the link is about or,what kinds\n            of information is found at url, or what is the importance of\n            the link\n        ', verbose_name='extended description'),
        ),
    ]
