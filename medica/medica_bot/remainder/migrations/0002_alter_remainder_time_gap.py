# Generated by Django 4.1.7 on 2023-03-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remainder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remainder',
            name='time_gap',
            field=models.CharField(max_length=16),
        ),
    ]
