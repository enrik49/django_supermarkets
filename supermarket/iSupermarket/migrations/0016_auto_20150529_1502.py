# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0015_auto_20150526_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 15, 2, 52, 598601, tzinfo=utc)),
        ),
    ]
