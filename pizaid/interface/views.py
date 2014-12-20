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
from django.views.decorators.csrf import csrf_exempt
import models

def index(request):
    with ControllerComm() as comm:
        status = {
            'network':  models.gather_network_info(comm),
            'power':    models.gather_power_info(comm),
            'storages': models.gather_storage_info(comm)
        }
    return render_to_response('interface/index.html', status)

@csrf_exempt
def settings(request):
    from django.http import HttpResponse
    with ControllerComm() as comm:
        if request.method == 'POST':
            post = request.POST
            comm.storage().join(post["name"], post["disk"])
            # TODO: need to redirect
            return HttpResponse("success!!", mimetype="text/plain")
        else:
            disk_ids = models.get_disk_ids(comm)
            return render_to_response(
                'interface/settings.html', {"disk_ids": disk_ids}
            )
