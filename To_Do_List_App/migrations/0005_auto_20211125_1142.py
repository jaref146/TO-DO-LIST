# Generated by Django 3.2.6 on 2021-11-25 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_Do_List_App', '0004_auto_20211125_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 25, 11, 42, 5, 868932)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='update_date_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
