# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iSupermarket', '0009_auto_20150501_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientSucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.ManyToManyField(to='iSupermarket.Client')),
                ('sucursal', models.ManyToManyField(to='iSupermarket.Sucursal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarcaClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.ManyToManyField(to='iSupermarket.Client')),
                ('marca', models.ManyToManyField(to='iSupermarket.Marca')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarcaSucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.ManyToManyField(to='iSupermarket.Marca')),
                ('sucursal', models.ManyToManyField(to='iSupermarket.Sucursal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='producte',
            name='Marca',
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='Companyia',
        ),
        migrations.AddField(
            model_name='producte',
            name='marca',
            field=models.ForeignKey(related_name='producte', to='iSupermarket.Marca', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='companyia',
            field=models.ForeignKey(related_name='sucursal', to='iSupermarket.Companyia', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 9, 26, 8, 520485, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
