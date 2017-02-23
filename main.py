# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
This module serves as a main entry point for the HashCode 2017.

Team Zynertia, GO!
"""

import sys

__author__ = "Xavi Moreno, Francesc Recasens, Marc López"
__credits__ = ['Xavi Moreno', 'Francesc Recasens', 'Marc López']

__version__ = "0.0.1"
__status__ = 'Development'

caches = []


def write_file(filename):
    with open(filename, 'w') as input_file:
        input_file.write(str(len(caches)))
        for cache in caches:
            input_file.write(
                cache.id + " " + cache.print_videos()
            )


def calculate_best_videos_for_cache():
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

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    read_file(input_filename)

    # TODO: Process data

    write_file(output_filename)

if __name__ == '__main__':
    main()
