# Generated by Django 3.1.7 on 2021-04-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0002_detection_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detection',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
