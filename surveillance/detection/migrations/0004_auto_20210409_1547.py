# Generated by Django 3.1.7 on 2021-04-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_auto_20210409_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
