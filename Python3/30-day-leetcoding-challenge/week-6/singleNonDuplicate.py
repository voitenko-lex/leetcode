#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element
appears exactly twice, except for one element which appears exactly once.
Find this single element that appears only once.

Example 1:
    Input: [1,1,2,3,3,4,4,8,8]
    Output: 2

Example 2:
    Input: [3,3,7,7,10,11,11]
    Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""

import unittest
from typing import List, Set, Tuple, Dict

import collections

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        return res


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(2, self.sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))

    def test_sample01(self):
        self.assertEqual(10, self.sol.singleNonDuplicate([3,3,7,7,10,11,11]))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))



