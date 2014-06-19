#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://amiq11.tumblr.com
# License:  MIT License
# Created:  2014-06-07
#
import dbus

class PizaidStorage:
    def __init__(self):
        self.sbus = dbus.SessionBus()
        self.myobj = self.sbus.get_object('com.pizaid.Controller',
                                     '/com/pizaid/controller/Storage')
        self.properties = dbus.Interface(self.myobj, 'com.pizaid.storage.Properties')
    def get_properties(self):
        return self.properties

