# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150414_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='principal_investigator',
            field=models.ForeignKey(to='app.PrincipalInvestigator'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampletracking',
            name='comment',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampletracking',
            name='samplestatus',
            field=models.ForeignKey(to='app.SampleStatus'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='basecallermetricspath',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='comment',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='lengthgraphpath',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='number_of_samples',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='outputrunfilepath',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='platesize',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='protocol',
            field=models.ForeignKey(blank=True, to='app.Protocol', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='qualityfiltermetricspath',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='qualitygraphpath',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='samples',
            field=models.ManyToManyField(to='app.Sample', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sequencingrun',
            name='technician',
            field=models.ForeignKey(blank=True, to='app.Technician', null=True),
            preserve_default=True,
        ),
    ]
