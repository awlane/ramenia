# Generated by Django 3.1.1 on 2020-09-28 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rameniaapp', '0003_auto_20200928_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=140)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('preferences', models.JSONField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='')),
                ('badges', models.ManyToManyField(blank=True, to='rameniaapp.Badge')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('RV', 'Review'), ('PF', 'Profile'), ('ND', 'Noodle')], max_length=2)),
                ('reason', models.CharField(choices=[('AD', 'Advertising'), ('HR', 'Harassment'), ('IC', 'Copyrighted or illegal content'), ('GS', 'Disgusting or disturbing content')], max_length=2)),
                ('status', models.CharField(choices=[('OP', 'Open'), ('ED', 'Resolved'), ('SP', 'Spam')], max_length=2)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('body', models.CharField(max_length=1000)),
                ('rating', models.IntegerField(choices=[(1, 'One Star'), (2, 'Two Star'), (3, 'Three Star'), (4, 'Four Star'), (5, 'Five Star')])),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.review')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rameniaapp.report')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.review')),
            ],
            bases=('rameniaapp.report',),
        ),
        migrations.CreateModel(
            name='ProfileReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rameniaapp.report')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.profile')),
            ],
            bases=('rameniaapp.report',),
        ),
        migrations.CreateModel(
            name='NoodleReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rameniaapp.report')),
                ('noodle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rameniaapp.noodle')),
            ],
            bases=('rameniaapp.report',),
        ),
    ]
