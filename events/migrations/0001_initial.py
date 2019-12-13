# Generated by Django 2.2.7 on 2019-11-14 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('event_title', models.CharField(max_length=2000)),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('event_stime', models.TimeField()),
                ('event_etime', models.TimeField()),
                ('event_address', models.CharField(max_length=2000)),
                ('event_content', models.TextField(blank=True)),
                ('event_cn', models.BooleanField()),
                ('event_s', models.BooleanField()),
            ],
        ),
    ]