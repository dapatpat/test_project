# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sim_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuinfos',
            name='sub_no',
        ),
        migrations.RemoveField(
            model_name='stuinfos',
            name='sub_score',
        ),
        migrations.AlterField(
            model_name='stuinfos',
            name='stu_duty',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stuinfos',
            name='stu_name',
            field=models.CharField(max_length=30),
        ),
    ]
