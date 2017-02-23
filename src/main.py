# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This module serves as a main entry point for the HashCode 2017.

Team Zynertia, GO!
"""

import operator
import sys

from src.CacheServer import CacheServer
from src.Endpoint import Endpoint
from src.Video import Video

__author__ = "Xavi Moreno, Francesc Recasens, Marc López"
__credits__ = ['Xavi Moreno', 'Francesc Recasens', 'Marc López']

__version__ = "0.0.1"
__status__ = 'Development'

caches = []
videos = []
endpoints = []


def write_file(filename):
    global caches

    with open(filename, 'w') as input_file:
        input_file.write(str(len(caches)) + "\n")

        for cache in caches:
            input_file.write(
                str(cache) + "\n"
            )


def calculate_best_videos_for_cache(cache):
    """
    :type cache: CacheServer
    """
    d_videos = {}
    for endpoint in cache.endpoints:
        for request in endpoint['endpoint'].requests:
            video_id = request['video']
            if video_id not in d_videos:
                d_videos[video_id] = request['requests']
            else:
                d_videos[video_id] += request['requests']

        # Now we have all the videos with their added requests (all requests that CAN be routed to this cache).
        # So we will just optimize the most videos possible.

        # TODO: Recursive algorithm to find the MOST SPACE USED (could be better solution)
        # TODO: Weights to determine if optimizing space is more worth than optimizing latencies

    sorted_videos = reversed(sorted(d_videos.items(), key=operator.itemgetter(1)))

    full = False
    for video in sorted_videos:
        video_id, request_count = video
        if full:
            break
        if cache.can_fit_video(videos[video_id].size):
            cache.add_video(video_id, videos[video_id].size)


def calculate_cache_priorities_per_video():
    pass


def read_file(file_name):
    with open(file_name, 'r') as f:
        l_caches = []
        l_videos = []
        videos, endpoints, request_descriptions, caches, cache_size = f.readline().split(' ')

        for i in xrange(0, int(caches)):
            l_caches.append(CacheServer(i, int(cache_size)))

        for i, size in enumerate([int(x) for x in f.readline().split(' ')]):
            l_videos.append(Video(i, size))

        endpoints = [Endpoint(_) for _ in xrange(int(endpoints))]

        #parse endpoint cfg
        for idx in xrange(len(endpoints)):
            v = f.readline().split(' ')
            ms = int(v[0])
            nu = int(v[1])
            endpoints[idx].add_latency(ms)

            for random_damn_index in xrange(nu):
                cache_index, latency = [int(x) for x in f.readline().split(' ')]
                endpoints[idx].add_latency(latency, cache_index)
                l_caches[cache_index].add_endpoint(endpoints[idx], latency)

        #parse video requests
        for idx in xrange(int(request_descriptions)):
            video_id, endpoint_id, num_requests = (int(x) for x in f.readline().split(' '))
            endpoints[endpoint_id].add_request(video_id, num_requests)

        return l_caches, endpoints, l_videos


def main():
    """
    I'll use this to comment the possible strategies.

    Strategy 1: Decide, independently for every cache server, the best videos to store (depending on requests and clients.
    Strategy 2: Same as above but every cache server knows the preceding cache server stored videos, so we can improve
    the speeds of only the videos that aren't being improved.
    Strategy 3: For every VIDEO, decide which cache is the most valiable. Assign priorities to every video and cache.
    Then caches decide how many videos can accept and order them depending on the priorities already given.
    Last Strategy: Optimize for every cache and video and enjoy the best damn caching system in the world.
    """
    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <input_filename> <output_filename>' % sys.argv[0])

    global caches, videos, endpoints

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    caches, endpoints, videos = read_file(input_filename)

    print caches
    for cache in caches:
        print cache.endpoints
    print endpoints
    print videos

    for cache in caches:
        calculate_best_videos_for_cache(cache)

    print "After assigning videos:"
    print caches

    write_file(output_filename)

if __name__ == '__main__':
    main()
