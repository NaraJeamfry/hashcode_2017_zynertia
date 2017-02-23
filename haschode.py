#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def main():
    pass


def read_file(file_name):
    with open(file_name, 'r') as f:

        videos, endpoints, request_descriptions, caches, cache_size = f.readline().split(' ')
        video_file_sizes = [int(x) for x in f.readline().split(' ')]
        endpoints = [[] for _ in range(int(endpoints))]
        #parse endpoint cfg
        for idx in range(len(endpoints)):
            v = f.readline().split(' ')
            ms = int(v[0])
            nu = int(v[1])
            endpoints[idx] = [ms, nu, []]
            for _ in range(nu):
                endpoints[idx][2].append(int(f.readline().split(' ')[1]))

        #parse video requests
        request_descriptions = [[] for _ in range(int(request_descriptions))]
        for idx in range(len(request_descriptions)):
            request_descriptions[idx] = [int(x) for x in f.readline().split(' ')]


        print videos, caches, caches
        print endpoints
        print request_descriptions




if __name__ == '__main__':
    main()
    read_file('sample.in')


    # for line in file:
    # for char in line.split(' '):
    # print char
