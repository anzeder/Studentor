# Generated by Django 3.2.6 on 2021-10-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20211017_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='question',
            field=models.TextField(),
        ),
    ]
