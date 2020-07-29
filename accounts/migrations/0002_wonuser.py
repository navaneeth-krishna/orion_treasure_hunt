# Generated by Django 3.0.7 on 2020-06-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WonUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_won', models.DateTimeField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('clue1solved', models.DateTimeField()),
                ('clue2solved', models.DateTimeField()),
            ],
        ),
    ]
