"""
Definition of models.
"""

from datetime import *
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PrincipalInvestigator(models.Model):
    user_account = models.ForeignKey(User, db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    institution = models.CharField(max_length=254)

    def __unicode__(self):
        return str(self.user_account)

class Laboratory(models.Model):
    """This models a Laboratory from which orders are received """
    name = models.CharField(max_length=254)
    principal_investigator = models.ForeignKey(PrincipalInvestigator, db_index=True)

    def __unicode__(self):
        return str(self.name)

class Technician(models.Model):
    technicianID = models.CharField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Apparatus(models.Model):
    """A machine that sequences DNA """
    machineID = models.CharField(max_length=254)

class Protocol(models.Model):
    """A protocol for sequencing """
    name = models.CharField(max_length=254)
    desc = models.TextField()
    referenceID = models.CharField(max_length=254)

class Organism(models.Model):
    """Organism from which the sample(s) are obtained """
    common = models.CharField(max_length=254)
    linnaean = models.CharField(max_length=254)
    strain = models.CharField(max_length=254)

    def __unicode__(self):
        return str(self.linnaean)+' '+str(self.strain)

class Order(models.Model):
    name=models.CharField(max_length=254)
    description=models.CharField(max_length=254)
    number_of_samples=models.IntegerField()

    def __unicode__(self):
        return str(self.name)

class Sample(models.Model):
    """A single sample's information"""
    sampleID = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    order = models.ForeignKey(Order, db_index=True, related_name='samples')
    ordered = models.DateTimeField('date created', default=datetime.now)
    received = models.DateTimeField(null=True, blank=True)
    laboratory = models.ForeignKey(Laboratory, db_index=True)
    protocolID = models.ForeignKey(Protocol, db_index=True, null=True, blank=True)
    region = models.IntegerField(null=True, blank=True)
    concentration_of_DNA = models.FloatField(null=True, blank=True)
    bead_count = models.IntegerField(null=True, blank=True)
    enrichment_percentage = models.IntegerField(null=True, blank=True)
    organism = models.ForeignKey(Organism, db_index=True)

    def __unicode__(self):
        return str(self.sampleID+'|'+str(self.name)+'|'+str(self.organism))

class Project(models.Model):
    """This models a particular Project under which orders are organized """
    projectID = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    laboratory = models.ForeignKey(Laboratory, db_index=True)
    samples = models.ManyToManyField(Sample, blank=True)

    def __unicode__(self):
        return str(self.name)

class SampleStatus(models.Model):
    _choices={'1': 'Received', '2': 'Sequencing', '3': 'Finished'}
    status = models.CharField(max_length=30, null=True, blank=True)

class SampleTracking(models.Model):
    """Mutable record tracks sample workflow    """
    sampleID = models.OneToOneField(Sample)
    samplestatus = models.ForeignKey(SampleStatus, db_index=True)
    technician = models.ForeignKey(Technician, db_index=True)
    timestamp = models.DateTimeField('date created', default=datetime.now)
    comment = models.CharField(max_length=254, null=True, blank=True)

class SequencingRun(models.Model):
    """Sequencing runs associated with machine - may contain multiple different orders' samples """
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    comment = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField('date created', default=datetime.now)
    technician = models.ForeignKey(Technician, db_index=True, null=True, blank=True)
    platesize = models.PositiveSmallIntegerField(null=True, blank=True)
    number_of_samples = models.IntegerField()
    samples = models.ManyToManyField(Sample, blank=True)
    protocol = models.ForeignKey(Protocol, db_index=True, null=True, blank=True)
    basecallermetricspath = models.CharField(max_length=254, null=True, blank=True)
    qualityfiltermetricspath = models.CharField(max_length=254, null=True, blank=True)
    qualitygraphpath = models.CharField(max_length=254, null=True, blank=True)
    lengthgraphpath = models.CharField(max_length=254, null=True, blank=True)
    outputrunfilepath = models.CharField(max_length=254, null=True, blank=True)


