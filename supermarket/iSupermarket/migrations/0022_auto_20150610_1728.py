# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0021_auto_20150610_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 17, 28, 42, 930874, tzinfo=utc)),
        ),
    ]
