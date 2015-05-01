# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0008_auto_20150501_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
