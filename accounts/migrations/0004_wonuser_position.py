# Generated by Django 3.0.7 on 2020-06-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200610_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='wonuser',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
