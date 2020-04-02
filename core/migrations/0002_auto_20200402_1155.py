# Generated by Django 3.0.4 on 2020-04-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='hey there', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='external_links',
            field=models.CharField(default='google.com', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='name',
            field=models.CharField(default='EVENT50', max_length=48),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='promotion',
            name='channel',
            field=models.CharField(max_length=20),
        ),
    ]