# Generated by Django 3.0.5 on 2020-05-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprof',
            name='delete_times',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
