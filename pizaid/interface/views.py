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

def index(request):
    status = {}
    # 通信が必要な内容はすべてwith句に収める必要がある
    with ControllerComm() as comm:
        names = comm.storage().get_names()
        status['ipv4'] = comm.network().get_ipv4()
        status['names'] = names
        status['total'] = comm.storage().get_capacity_kb(names[0])
        status['used'] = comm.storage().get_usage_kb(names[0])
        status['usage'] = comm.storage().get_usage_percent(names[0])
        status['ac'] = comm.power().is_ac_plugin()
    return render_to_response('interface/index.html')

def settings(request):
    return render_to_response('interface/settings.html')
