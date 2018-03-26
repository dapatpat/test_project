# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('area', models.CharField(max_length=20)),
                ('parea', models.ForeignKey(blank=True, null=True, to='area.areas')),
            ],
            options={
                'db_table': 'areas',
            },
        ),
    ]
