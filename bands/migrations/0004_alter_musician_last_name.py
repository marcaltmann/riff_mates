# Generated by Django 5.0.6 on 2024-06-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='last_name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
