# Generated by Django 2.1.15 on 2020-06-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmastore', '0015_presciptionimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presciptionimages',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
