# Generated by Django 3.0.7 on 2020-06-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='clue_no',
            field=models.IntegerField(default=0),
        ),
    ]
