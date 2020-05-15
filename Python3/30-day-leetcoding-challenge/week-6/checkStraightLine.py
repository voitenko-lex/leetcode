#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 14
    Output: false
"""

import unittest
from typing import List, Set, Tuple, Dict

import math

class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    #     if num % 10 in (2,3,7,8):
    #         return False
    #     start = 0
    #     step = 1
    #     while True:
    #         start += step
    #         if start == num:
    #             return True
    #         elif start > num:
    #             return False
    #         step += 2

        
    def isPerfectSquare(self, num: int) -> bool:
        if num % 10 in (2,3,7,8):
            return False
        l = 1
        r = num
        while(r >= l):
            mid = int((l + r) / 2)
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                r = mid - 1
            else:
                l = mid + 1
        return False


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(True, self.sol.isPerfectSquare(1))

    def test_sample01(self):
        self.assertEqual(False, self.sol.isPerfectSquare(14))

    def test_sample02(self):
        self.assertEqual(True, self.sol.isPerfectSquare(16))

    def test_sample03(self):
        self.assertEqual(False, self.sol.isPerfectSquare(2147483647))

    
if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        # sol = Solution()
        # print(sol.isPerfectSquare(14))

        a = (1,4,5,6,9,0)
        print(type(a))

