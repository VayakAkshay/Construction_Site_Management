# Generated by Django 3.2.18 on 2023-04-14 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentmachinerydata',
            name='Details',
        ),
        migrations.AlterField(
            model_name='expensedata',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 14, 11, 35, 31, 613755)),
        ),
        migrations.AlterField(
            model_name='incomedata',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 14, 11, 35, 31, 612218)),
        ),
    ]