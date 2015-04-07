# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloRest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='boxReceiver',
            field=models.ForeignKey(related_name='boxReceiver', to='helloRest.Box'),
        ),
        migrations.AlterField(
            model_name='hello',
            name='boxSender',
            field=models.ForeignKey(related_name='boxSender', to='helloRest.Box'),
        ),
    ]
