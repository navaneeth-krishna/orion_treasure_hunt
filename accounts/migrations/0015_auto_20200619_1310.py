# Generated by Django 3.0.7 on 2020-06-19 07:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200619_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='dead',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='cluedead',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 20, 7, 40, 34, 489483, tzinfo=utc), null=True),
        ),
    ]