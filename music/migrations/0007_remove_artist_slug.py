# Generated by Django 4.2.5 on 2023-11-17 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_artist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='slug',
        ),
    ]