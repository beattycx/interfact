# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150414_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequencingrun',
            old_name='desc',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='sample',
            name='bead_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='concentration_of_DNA',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='enrichment_percentage',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='projectIDs',
            field=models.ManyToManyField(to='app.Project', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='protocolID',
            field=models.ForeignKey(blank=True, to='app.Protocol', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='received',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='region',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='basecallermetricspath',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='comment',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='lengthgraphpath',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='outputrunfilepath',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='platesize',
            field=models.PositiveSmallIntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='protocol',
            field=models.ForeignKey(to='app.Protocol', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='qualityfiltermetricspath',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='qualitygraphpath',
            field=models.CharField(max_length=254, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='samples',
            field=models.ManyToManyField(to='app.Sample', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='technician',
            field=models.ForeignKey(to='app.Technician', blank=True),
            preserve_default=True,
        ),
    ]
