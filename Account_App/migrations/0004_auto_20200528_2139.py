# Generated by Django 3.0.5 on 2020-05-28 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_App', '0003_auto_20200528_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='icon',
            field=models.ImageField(default='static/image/default_icon.jpg', upload_to='icon'),
        ),
    ]