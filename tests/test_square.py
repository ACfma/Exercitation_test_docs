# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:23:36 2020

@author: Andrea
"""
import unittest

from Squareup.core import square

class TestCore(unittest.TestCase):
    '''Testing the core'''
    def test_float(self):
        '''Testing...'''
        self.assertAlmostEqual(square(2.),4)


if __name__=='__main__':
    unittest.main()
    