# Generated by Django 4.1.7 on 2023-03-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='Male', max_length=50),
        ),
    ]
