# Generated by Django 2.0.6 on 2018-07-03 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camapp', '0011_delete_ipaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipaddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=500)),
                ('group_id', models.CharField(default='1', max_length=100)),
            ],
        ),
    ]
