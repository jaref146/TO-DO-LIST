# Generated by Django 3.2.6 on 2021-11-24 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(blank=True, max_length=200, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 24, 18, 27, 13, 978370))),
            ],
        ),
    ]