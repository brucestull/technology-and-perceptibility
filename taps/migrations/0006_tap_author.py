# Generated by Django 3.2 on 2022-04-03 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taps', '0005_alter_tap_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='taps', to='users.customuser'),
            preserve_default=False,
        ),
    ]
