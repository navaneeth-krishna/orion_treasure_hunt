# Generated by Django 3.0.7 on 2020-06-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200617_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='cluedead',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]