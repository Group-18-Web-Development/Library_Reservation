# Generated by Django 3.0.5 on 2020-05-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_App', '0004_auto_20200528_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='icon',
            field=models.ImageField(default='icon/default_icon.jpg', upload_to='icon'),
        ),
    ]