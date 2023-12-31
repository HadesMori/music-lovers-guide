# Generated by Django 4.2.5 on 2023-11-17 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_remove_artist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='members',
        ),
        migrations.AddField(
            model_name='artist',
            name='band',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='music.band'),
            preserve_default=False,
        ),
    ]
