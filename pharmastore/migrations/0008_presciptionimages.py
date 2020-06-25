# Generated by Django 2.1.15 on 2020-06-18 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmastore', '0007_auto_20200617_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresciptionImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmastore.DrugRequest')),
            ],
        ),
    ]