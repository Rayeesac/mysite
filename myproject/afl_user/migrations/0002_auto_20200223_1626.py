# Generated by Django 2.2.7 on 2020-02-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afl_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
