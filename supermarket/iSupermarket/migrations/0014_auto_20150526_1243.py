# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0013_auto_20150526_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 12, 43, 33, 775181, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
