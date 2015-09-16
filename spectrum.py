# -*- coding: utf-8 -*-

import os

import numpy as np


class Spectrum:
    def __init__(self, filename):
        self.path = os.path.abspath(filename)
        self.basename = os.path.basename(filename)
        try:
            self.import_scn(filename)
        except:
            self.name = ''
            self.header = []
            self.mass_values = np.array([])

    def import_scn(self, filename):
        skiprows = 5
        self.name = os.path.basename(filename)
        with open(filename, 'r') as f:
            self.header = [f.readline() for _ in range(skiprows)]
        if self.name:
            self.mass_values = np.loadtxt(filename, skiprows=skiprows)
