#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Francesc Recasens'


class CacheServer(object):
    def __init__(self, num, space):
        self.id = num
        self.max_capacity = self.free_space = space
        self.videos = {}
        self.endpoints = {}

    def __str__(self):
        return str(self.id) + " " + self.print_videos()

    def __repr__(self):
        return str(self)

    # ----- Treating videos -----
    def can_fit_video(self, size):
        return self.free_space - size >= 0

    def add_video(self, id_video, video_size):
        if self.can_fit_video(video_size):
            self.free_space = self.free_space - video_size
            if not self.find_video(id_video):
                self.videos[id_video] = video_size

    def find_video(self, id_video):
        return self.videos.get(id_video, None)

    def remove_video(self, id_video):
        del self.videos[id_video]

    def print_videos(self):
        return ' '.join(self.videos.keys())

    # ----- Treating connected endpoints :) -----
    def add_endpoint(self, endpoint, latency):
        self.endpoints[endpoint] = latency
