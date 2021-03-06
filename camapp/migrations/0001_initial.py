# Generated by Django 2.0.6 on 2018-06-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fraud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('personId', models.IntegerField(default=-1)),
                ('t1', models.TimeField(auto_now_add=True)),
                ('t2', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emailId', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=12)),
                ('Image_1', models.FileField(upload_to='')),
                ('Image_2', models.FileField(upload_to='')),
                ('Image_3', models.FileField(upload_to='')),
                ('Image_4', models.FileField(upload_to='')),
                ('Image_5', models.FileField(upload_to='')),
                ('Train_status', models.CharField(default='n', max_length=1)),
                ('person_id', models.CharField(default='', max_length=500)),
                ('person_present_status', models.BooleanField(default=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TableAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('personId', models.IntegerField(default=-1)),
                ('ts', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
