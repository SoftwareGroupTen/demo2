# Generated by Django 2.2.12 on 2020-04-26 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkPublish', '0003_auto_20200416_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='courseNum',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
