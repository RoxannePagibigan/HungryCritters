# Generated by Django 2.2 on 2021-06-04 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210604_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 4, 11, 50, 13, 839734)),
        ),
    ]
