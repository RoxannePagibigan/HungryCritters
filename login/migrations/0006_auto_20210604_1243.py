# Generated by Django 2.2 on 2021-06-04 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210604_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 4, 12, 43, 8, 754050)),
        ),
    ]
