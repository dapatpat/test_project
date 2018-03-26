# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stuInfos',
            fields=[
                ('stu_no', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=10)),
                ('stu_gender', models.BooleanField()),
                ('stu_duty', models.CharField(max_length=20, null=True)),
                ('stu_age', models.IntegerField()),
                ('sub_score', models.FloatField()),
            ],
            options={
                'db_table': 'stuInfos',
            },
        ),
        migrations.CreateModel(
            name='subInfos',
            fields=[
                ('sub_no', models.IntegerField(primary_key=True, serialize=False, auto_created=True)),
                ('sub_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'subInfos',
            },
        ),
        migrations.AddField(
            model_name='stuinfos',
            name='sub_no',
            field=models.ForeignKey(to='sim_system.subInfos'),
        ),
    ]
