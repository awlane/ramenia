# Generated by Django 3.1.2 on 2020-10-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rameniaapp', '0014_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='noodles',
            field=models.ManyToManyField(blank=True, to='rameniaapp.Noodle'),
        ),
    ]
