# Generated by Django 2.2.12 on 2020-05-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkPublish', '0006_auto_20200502_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='Homework_title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
