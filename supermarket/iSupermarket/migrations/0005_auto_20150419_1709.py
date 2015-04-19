# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0004_auto_20150419_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.TextField(max_length=20),
            preserve_default=True,
        ),
    ]
