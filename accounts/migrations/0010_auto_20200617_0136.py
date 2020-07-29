# Generated by Django 3.0.7 on 2020-06-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200611_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='clue10solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue11solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue12solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue13solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue14solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue15solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue4solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue5solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue6solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue7solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue8solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='clue9solved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue10solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue11solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue12solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue13solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue14solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue15solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue4solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue5solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue6solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue7solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue8solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='wonuser',
            name='clue9solved',
            field=models.DateTimeField(null='True'),
            preserve_default='True',
        ),
    ]