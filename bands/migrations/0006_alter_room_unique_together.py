# Generated by Django 5.0.6 on 2024-06-07 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bands", "0005_musician_bands_music_last_na_979e82_idx"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="room",
            unique_together={("name", "venue")},
        ),
    ]