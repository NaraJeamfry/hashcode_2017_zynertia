#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Francesc Recasens'

DATACENTER_KEY = -1


class Endpoint(object):

    def __init__(self, num):
        self.id = num
        self.latencies = []
        self.requests = []
        self.datacenter_latency = 0

    def __str__(self):
        return "Endpoint %i (%i caches, %i videos) - datacenter: %i ms" % (
            self.id,
            len(self.latencies),
            len(self.requests),
            self.datacenter_latency
        )

    def __repr__(self):
        return str(self)

    def add_request(self, id_video, num_requests):
        self.requests.append({'video': id_video, 'requests': num_requests})

    def add_latency(self, latency, cache=DATACENTER_KEY):
        if cache == DATACENTER_KEY:
            self.datacenter_latency = latency
        else:
            self.latencies.append({'cache': cache, 'latency': latency})

    def get_latency_for_cache(self, cache=DATACENTER_KEY):
        if cache == DATACENTER_KEY:
            return self.datacenter_latency
        else:
            latencies = filter(lambda e: e['cache'] == cache, self.latencies)
            if len(latencies) > 0:
                return latencies[0]['latency']
            else:
                return -1

    def get_requests_for_video(self, video):
        videos = filter(lambda e: e['video'] == video, self.requests)
        if len(videos) > 0:
            return videos[0]['requests']
        else:
            return -1
