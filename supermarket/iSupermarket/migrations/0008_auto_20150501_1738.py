# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0007_auto_20150419_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
