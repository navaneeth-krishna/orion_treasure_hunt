# Generated by Django 3.0.7 on 2020-06-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200611_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='team_mate_contact',
            field=models.CharField(blank='True', default='', max_length=15, null='True'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='team_mate_name',
            field=models.CharField(blank='True', default='', max_length=50, null='True'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_contact',
            field=models.CharField(blank='True', default='', max_length=15, null='True'),
        ),
    ]
