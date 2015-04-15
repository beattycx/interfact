# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('machineID', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common', models.CharField(max_length=254)),
                ('linnaean', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrincipalInvestigator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('institution', models.CharField(max_length=254)),
                ('user_account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectID', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('laboratoryID', models.ForeignKey(to='app.Laboratory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('desc', models.TextField()),
                ('referenceID', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sampleID', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('received', models.DateTimeField()),
                ('region', models.IntegerField()),
                ('concentration_of_DNA', models.FloatField()),
                ('bead_count', models.IntegerField()),
                ('enrichment_percentage', models.IntegerField()),
                ('laboratory', models.ForeignKey(to='app.Laboratory')),
                ('organism', models.ForeignKey(to='app.Organism')),
                ('projectIDs', models.ManyToManyField(to='app.Project')),
                ('protocolID', models.ForeignKey(to='app.Protocol')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SampleTracking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('samplestatus', models.CharField(max_length=254)),
                ('timestamp', models.DateTimeField()),
                ('comment', models.CharField(max_length=254)),
                ('sampleID', models.OneToOneField(to='app.Sample')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SequencingRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('desc', models.CharField(max_length=254)),
                ('comment', models.CharField(max_length=254)),
                ('date', models.DateTimeField()),
                ('platesize', models.PositiveSmallIntegerField()),
                ('number_of_samples', models.PositiveIntegerField()),
                ('basecallermetricspath', models.CharField(max_length=254)),
                ('qualityfiltermetricspath', models.CharField(max_length=254)),
                ('qualitygraphpath', models.CharField(max_length=254)),
                ('lengthgraphpath', models.CharField(max_length=254)),
                ('outputrunfilepath', models.CharField(max_length=254)),
                ('protocol', models.ForeignKey(to='app.Protocol')),
                ('samples', models.ManyToManyField(to='app.Sample')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technicianID', models.CharField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sequencingrun',
            name='technician',
            field=models.ForeignKey(to='app.Technician'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sampletracking',
            name='technician',
            field=models.ForeignKey(to='app.Technician'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='laboratory',
            name='principal_investigator',
            field=models.OneToOneField(to='app.PrincipalInvestigator'),
            preserve_default=True,
        ),
    ]
