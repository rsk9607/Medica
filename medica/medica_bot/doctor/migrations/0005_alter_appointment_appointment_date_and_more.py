# Generated by Django 4.1.7 on 2023-04-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_reason',
            field=models.TextField(blank=True),
        ),
    ]
