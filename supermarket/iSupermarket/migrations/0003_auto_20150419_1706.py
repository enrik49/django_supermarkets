# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0002_auto_20150419_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone',
        ),
        migrations.AddField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(null=True, verbose_name=b'date registred'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companyia',
            name='idNumber',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companyia',
            name='name',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='marca',
            name='name',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producte',
            name='name',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='name',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
