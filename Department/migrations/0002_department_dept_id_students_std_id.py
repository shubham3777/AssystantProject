# Generated by Django 4.0.2 on 2022-02-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dept_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='std_id',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
