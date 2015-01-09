#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RfModbusError(Exception):

    def __init__(self, msg, detail=None):
        Exception.__init__(self)
        self.msg = msg
        self.detail = detail

    def __str__(self):
        return u"%s (%s)" % (self.msg, self.detail)

    def __unicode__(self):
        return u"%s (%s)" % (self.msg, self.detail)
