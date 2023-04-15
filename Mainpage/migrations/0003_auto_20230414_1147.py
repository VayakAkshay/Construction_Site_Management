# Generated by Django 3.2.18 on 2023-04-14 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0002_auto_20230414_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedata',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 14, 11, 47, 2, 624391)),
        ),
        migrations.AlterField(
            model_name='incomedata',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 14, 11, 47, 2, 624391)),
        ),
        migrations.AlterField(
            model_name='transportdata',
            name='vehical_number',
            field=models.TextField(default='', max_length=100),
        ),
    ]
