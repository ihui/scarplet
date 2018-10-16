import unittest

import numpy as np
from osgeo import gdal, osr, ogr

from scipy.special import erf

from context import scarplet
import scarplet as sl
from scarplet.WindowedTemplate import Scarp, Channel

DEFAULT_EPSG = 32610 # UTM 10N


class ScarpTestCase(unittest.TestCase):


    def setUp(self):
    
        self.obj = Scarp(100, 10, 0, 100, 100, 1)

    def test_template(self):

        test = self.obj.template()
        true = np.load('results/scarp_template.npy')

        self.assertTrue(np.allclose(test, true), "Scarp template function is \
                        incorrect")

    def test_template_numexpr(self):

        test = self.obj.template_numexpr()
        true = np.load('results/scarp_template_numexpr.npy')

        self.assertTrue(np.allclose(test, true), "Scarp template function is \
                        incorrect")


class ChannelTestCase(unittest.TestCase):


    def setUp(self):
    
        self.obj = Channel(100, 0.1, 0, 100, 100, 1)

    def test_template(self):

        test = self.obj.template()
        true = np.load('results/channel_template.npy')

        self.assertTrue(np.allclose(test, true), "Channel template function is \
                        incorrect")
