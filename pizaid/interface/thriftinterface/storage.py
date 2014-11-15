#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-08-09
#

class PizaidStorage:
    def __init__(self, client):
        self.client = client
    def storage_group_list(self):
        return self.client.storage_storage_group_list()
    def capacity_kb(self, name):
        return self.client.storage_capacity_kb(name)
    def usage_kb(self, name):
        return self.client.storage_usage_kb(name)
    def usage_percent(self, name):
        return self.client.storage_usage_percent(name)
    def is_sync(self):
        return self.client.storage_is_sync()
    def join(self, name, disk):
        return self.client.storage_join(name, disk)
    def disk_list(self, name):
        return self.client.storage_disk_list(name)
    def disk_id(self, disk):
        return self.client.storage_disk_id(disk)
    def disk_size(self, disk):
        return self.client.storage_disk_size(disk)
    def disk_port(self, disk):
        return self.client.storage_disk_port(disk)
