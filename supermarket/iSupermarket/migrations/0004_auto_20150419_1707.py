# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0003_auto_20150419_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='lastName',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
