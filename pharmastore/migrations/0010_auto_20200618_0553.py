# Generated by Django 2.1.15 on 2020-06-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmastore', '0009_auto_20200618_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drugrequest',
            name='images',
        ),
        migrations.AddField(
            model_name='drugrequest',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.DeleteModel(
            name='PresciptionImages',
        ),
    ]
