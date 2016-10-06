#!/usr/bin/env python3

import unittest

from euclidean import euclideanGCD, extendedEuclidean


class test_euclideanGCD(unittest.TestCase):
    
    def test_0(self):
        self.assertEqual(euclideanGCD(0,0), 0)
        self.assertEqual(euclideanGCD(0,1), 1)
        self.assertEqual(euclideanGCD(1,0), 1)
        self.assertEqual(euclideanGCD(0,12), 12)
        self.assertEqual(euclideanGCD(12,0), 12)
    
    def test_1(self):
        self.assertEqual(euclideanGCD(1,12), 1)
        self.assertEqual(euclideanGCD(12,1), 1)
    
    def test_big_factors(self):
        self.assertEqual(euclideanGCD(1406700, 164115  ), 23445)
        self.assertEqual(euclideanGCD(164115,  1406700 ), 23445)
        self.assertEqual(euclideanGCD(55534,   434334  ), 2)
        self.assertEqual(euclideanGCD(434334,  55534   ), 2)
        self.assertEqual(euclideanGCD(30315475,24440870), 31415)
        self.assertEqual(euclideanGCD(24440870,30315475), 31415)
        self.assertEqual(euclideanGCD(37279462087332,366983722766), 564958)
        self.assertEqual(euclideanGCD(366983722766,37279462087332), 564958)
    
    def test_big_primes(self):
        self.assertEqual(euclideanGCD(2921802413,20358439), 1)
        self.assertEqual(euclideanGCD(20358439,2921802413), 1)
        self.assertEqual(euclideanGCD(85796527,34775062331),1)
        self.assertEqual(euclideanGCD(34775062331,85796527),1)

class test_extendedEuclidean(unittest.TestCase):
    
    pass



if __name__ == '__main__':
    unittest.main()
