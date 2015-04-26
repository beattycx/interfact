__author__ = 'Xavier'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
from django.utils.datastructures import SortedDict


def yield_to_template(form_instance, model_object, exclude=(), append=()):
    i=0
    sd=SortedDict()

    for j in append:
        try:
            sdvalue={'label':j.capitalize(),
                     'fieldvalue':model_object.__getattribute__(j)}
            sd.insert(i, j, sdvalue)
            i+=1
        except(AttributeError):
            pass

    for k,v in form_instance.fields.items():
        sdvalue={'label':"", 'fieldvalue':""}
        if not exclude.__contains__(k):
            if v.label is not None:
                sdvalue = {'label':v.label,
                           'fieldvalue': model_object.__getattribute__(k)}
            else:
                sdvalue = {'label':k,
                           'fieldvalue': model_object.__getattribute__(k)}
            sd.insert(i, k, sdvalue)
            i+=1
    return sd