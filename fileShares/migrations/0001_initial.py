# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('downloadDocount', models.IntegerField(verbose_name='浏览次数', default=0)),
                ('code', models.CharField(verbose_name='code', max_length=8)),
                ('dateTime', models.DateTimeField(default=datetime.datetime(2019, 5, 13, 21, 8, 39, 839179))),
                ('path', models.CharField(verbose_name='路径', max_length=32)),
                ('name', models.CharField(verbose_name='文件名', max_length=32)),
                ('fileSize', models.CharField(verbose_name='大小', max_length=10)),
                ('PCIP', models.CharField(verbose_name='地址', max_length=32, default='')),
            ],
            options={
                'verbose_name': 'download',
                'db_table': 'download',
            },
        ),
    ]
