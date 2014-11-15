#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-08-09
#

from django.shortcuts import render_to_response
from thriftinterface.controllercomm import ControllerComm
import models

def index(request):
    with ControllerComm() as comm:
        status = {
            'network':  models.gather_network_info(comm),
            'power':    models.gather_power_info(comm),
            'storages': models.gather_storage_info(comm)
        }
    return render_to_response('interface/index.html', status)

def settings(request):
    return render_to_response('interface/settings.html')
