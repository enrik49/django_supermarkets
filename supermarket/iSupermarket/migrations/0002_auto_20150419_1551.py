# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0001_initial'),
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
        migrations.AddField(
            model_name='producte',
            name='Marca',
            field=models.ForeignKey(related_name='producte', to='iSupermarket.Marca', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='Companyia',
            field=models.ForeignKey(related_name='sucursal', to='iSupermarket.Companyia', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='StateOrProvince',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='country',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='location',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='zipCode',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
