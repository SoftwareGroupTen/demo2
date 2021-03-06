# Generated by Django 2.2.12 on 2020-05-05 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HomeworkPublish', '0006_auto_20200502_2011'),
        ('upload', '0002_auto_20200505_1104')
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.FloatField(null=True)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='HomeworkPublish.Homework')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
