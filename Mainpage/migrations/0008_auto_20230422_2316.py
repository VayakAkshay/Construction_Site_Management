# Generated by Django 3.2.18 on 2023-04-22 17:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Mainpage', '0007_auto_20230422_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedata',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 22, 23, 16, 24, 974929)),
        ),
        migrations.AlterField(
            model_name='incomedata',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 22, 23, 16, 24, 971413)),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='manager_user_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
