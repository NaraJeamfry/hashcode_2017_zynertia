#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from CacheServer import CacheServer
from Endpoint import Endpoint

def main():
    pass


def read_file(file_name):
    with open(file_name, 'r') as f:
        l_caches = []
        videos, endpoints, request_descriptions, caches, cache_size = f.readline().split(' ')

        for i in xrange(0, int(caches)):
            l_caches.append(CacheServer(i, int(cache_size)))

        video_file_sizes = [int(x) for x in f.readline().split(' ')]
        endpoints = [Endpoint(_) for _ in xrange(int(endpoints))]

        #parse endpoint cfg
        for idx in xrange(len(endpoints)):
            v = f.readline().split(' ')
            ms = int(v[0])
            nu = int(v[1])
            endpoints[idx].add_latency(ms)

            for cache_index in xrange(nu):
                endpoints[idx].add_latency(int(f.readline().split(' ')[1]), cache_index)

        #parse video requests
        for idx in xrange(int(request_descriptions)):
            video_id, endpoint_id, num_requests = (int(x) for x in f.readline().split(' '))
            endpoints[endpoint_id].add_request(video_id, num_requests)



        return l_caches, endpoints




if __name__ == '__main__':
    main()
    read_file('sample.in')


    # for line in file:
    # for char in line.split(' '):
    # print char
