# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This module serves as a main entry point for the HashCode 2017.

Team Zynertia, GO!
"""

import sys

from CacheServer import CacheServer
from Endpoint import Endpoint

__author__ = "Xavi Moreno, Francesc Recasens, Marc López"
__credits__ = ['Xavi Moreno', 'Francesc Recasens', 'Marc López']

__version__ = "0.0.1"
__status__ = 'Development'

caches = []


def write_file(filename):
    global caches

    with open(filename, 'w') as input_file:
        input_file.write(str(len(caches)) + "\n")

        for cache in caches:
            input_file.write(
                str(cache) + "\n"
            )


def calculate_best_videos_for_cache(cache):
    pass


def calculate_cache_priorities_per_video():
    pass


def read_file(filename):
    pass


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

    global caches

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    read_file(input_filename)

    caches = [CacheServer(0, 100), CacheServer(1, 100)]

    for cache in caches:
        calculate_best_videos_for_cache(cache)

    caches[0].add_video(1, 100)
    caches[0].add_video(2, 100)
    caches[1].add_video(3, 20)
    caches[1].add_video(4, 30)

    write_file(output_filename)

if __name__ == '__main__':
    main()
