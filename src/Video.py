#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Francesc Recasens'


class Video(object):
    def __init__(self, num, size):
        self.id = num
        self.size = size

    def __str__(self):
        return "%i (%i MB)" % (self.id, self.size)

    def __repr__(self):
        return str(self)
