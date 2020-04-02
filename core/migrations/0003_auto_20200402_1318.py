# Generated by Django 3.0.4 on 2020-04-02 13:18

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200402_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 2, 13, 17, 41, 868977, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Range Filter'),
        ),
        migrations.AddField(
            model_name='eventstatus',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventstatus',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Range Filter'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventtype',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Range Filter'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Range Filter'),
        ),
    ]