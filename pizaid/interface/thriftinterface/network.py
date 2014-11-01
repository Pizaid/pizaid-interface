#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-08-09
#

class PizaidNetwork:
    def __init__(self, client):
        self.client = client
    def ipv4(self):
        return self.client.network_ipv4()
    def ipv6(self):
        return self.client.network_ipv6()
