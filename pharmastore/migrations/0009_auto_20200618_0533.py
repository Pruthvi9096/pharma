# Generated by Django 2.1.15 on 2020-06-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmastore', '0008_presciptionimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presciptionimages',
            name='request',
        ),
        migrations.AddField(
            model_name='drugrequest',
            name='images',
            field=models.ManyToManyField(blank=True, to='pharmastore.PresciptionImages'),
        ),
    ]