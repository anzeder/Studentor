# Generated by Django 3.2.6 on 2021-10-21 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], default='m', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobbies',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='strong_at',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
