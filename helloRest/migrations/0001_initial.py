# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('spin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('boxReceiver', models.ForeignKey(related_name='box_receiver', to='helloRest.Box')),
                ('boxSender', models.ForeignKey(related_name='box_sender', to='helloRest.Box')),
            ],
        ),
    ]
