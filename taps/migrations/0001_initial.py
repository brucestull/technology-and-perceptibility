# Generated by Django 3.2 on 2022-04-01 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='short title for the url', max_length=200)),
                ('description', models.CharField(help_text='detailed description of the content of the url', max_length=300, verbose_name='url description')),
            ],
        ),
    ]
