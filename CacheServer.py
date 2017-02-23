#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Francesc Recasens'


class CacheServer(object):
    def __init__(self, num, space):
        self.id = num
        self.max_capacity = self.free_space = space
        self.videos = []

    def can_fit_video(self, size):
        return self.free_space - size >= 0

    def add_video(self, id_video, video_size):
        if self.can_fit_video(video_size):
            self.free_space = self.free_space - video_size
            if not self.find_video(id_video):
                self.videos.append({'id': id_video, 'space': video_size})

    def find_video(self, id_video):
        l_videos = filter(lambda e: e['id'] == id_video, self.videos)
        if len(l_videos) > 0:
            return l_videos[0]
        else:
            return None

    def remove_video(self, id_video):
        video = self.find_video(id_video)
        if video:
            self.free_space += video['space']
            self.videos.remove(video)

    def print_videos(self):
        ids = map(lambda e: str(e['id']), self.videos)
        return ' '.join(ids)

    def __str__(self):
        return str(self.id) + " " + self.print_videos()
