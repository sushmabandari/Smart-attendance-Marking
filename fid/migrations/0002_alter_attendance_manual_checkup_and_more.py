# Generated by Django 4.2.3 on 2023-12-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='manual_checkup',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='review',
            field=models.BooleanField(null=True),
        ),
    ]
