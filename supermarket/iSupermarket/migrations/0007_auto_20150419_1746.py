# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0006_auto_20150419_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='lastName',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=9, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(null=True, verbose_name=b'date registred'),
            preserve_default=True,
        ),
    ]
