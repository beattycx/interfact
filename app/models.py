"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Laboratory(models.Model):
    """This models a Laboratory from which orders are received """
    def __init__(self):
        name=''

class Project(models.Model):
    """This models a particular Project under which orders are organized """
    def __init__(self):
        name=''

class Sample(models.Model):
    """A single run"""
    def __init__(self):
        name=''

class Apparatus(models.Model):
    """A machine that sequences DNA """
    def __init__(self):
        name=''

class Project(models.Model):
    def __init__(self):
        name=''

class Protocol(models.Model):
    def __init__(self):
        name=''

class Organism(models.Model):
    def __init__(self):
        name=''