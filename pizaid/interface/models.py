#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from thriftinterface.controllercomm import ControllerComm

def gather_storage_info(comm):
    storage_info = {}
    for group_name in comm.storage().storage_group_list():
        storage_info[group_name] = {
            'capacity_kb': comm.storage().capacity_kb(group_name),
            'usage_kb': comm.storage().usage_kb(group_name),
            'usage_percent': comm.storage().usage_percent(group_name),
            'disks': []
        }
        for disk in comm.storage().disk_list(group_name):
            info = {
                'id': comm.storage().disk_id(disk),
                'size': comm.storage().disk_size(disk),
                'port': comm.storage().disk_port(disk)
            }
            storage_info[group_name]['disks'].append(info)
    return storage_info

def gather_network_info(comm):
    network_info = {
        'ipv4': comm.network().ipv4(),
        'ipv6': comm.network().ipv6()
    }
    return network_info

def gather_power_info(comm):
    power_info = {
        'is_ac_on': comm.power().is_ac_plugin(),
        'battery_percent': comm.power().battery_percent()
    }
    return power_info

