# -*- coding: utf-8 -*-

from Tools import *
from math import ceil
from abc import ABC

from map.Tileset import *
import pygame

#  _________________________________________________________ #
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ define file class ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ #

class Params(ABC):

    window_size = (1200, 800)
    map_size = (120, 80)  # default = (600, 400)
    map_tilesize = round(window_size[0] / map_size[0])  # default = 1
    map_stepping = 16  # default = 10
    map_freq_multiplier = 0.6  # default = 0.7
    map_octaves = 64  # default = 64

    map_min_tilesize = 1  # default = 2
    map_max_tilesize = 40  # default = 40

    # height < map_waterlevel = water
    # height < map_grasslevel && > map_waterlevel = grass
    # height > map_grasslevel = mountain
    map_waterlevel = ceil(map_stepping * 0.45)  # default = ceil(map_stepping * 0.45)
    map_grasslevel = ceil(map_stepping * 0.65)  # default = ceil(map_stepping * 0.65)

    map_current_offset = (0, 0)
    map_add_surface_offset = (0, 0)  # additional surface offset (relative to current offset)
    win_render_margin = 40           # rendered margin around the visible map - should be map_max_tilesize

    buffer_antialiasing = True         # False = better performance
    buffer_color_key = (255, 0, 255)   # the color that will become transparent when rendered

    @staticmethod
    def calc_min_tilesize(_size):
        # Params.map_min_tilesize = Tools.clip(max(ceil((_size[0] / Params.map_size[0]) / 2) * 2,
        #                                          ceil((_size[1] / Params.map_size[1]) / 2) * 2), 4, 40)
        if Params.map_tilesize < Params.map_min_tilesize:
            Params.map_tilesize = Params.map_min_tilesize

    @staticmethod
    def increase_tilesize():
            Params.map_tilesize = Tools.clip(Params.map_tilesize + 1, Params.map_min_tilesize, Params.map_max_tilesize)

    @staticmethod
    def decrease_tilesize():
            Params.map_tilesize = Tools.clip(Params.map_tilesize - 1, Params.map_min_tilesize, Params.map_max_tilesize)
