#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Majority Element

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
    Input: [3,2,3]
    Output: 3

Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2

"""

import unittest
from typing import List, Set, Tuple, Dict

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        # print(freq)
        majority_n = len(nums)/2
        for el in freq:
            if freq[el]>=majority_n:
                return el



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(3, self.sol.majorityElement([3,2,3]))

    def test_sample01(self):
        self.assertEqual(2, self.sol.majorityElement([2,2,1,1,1,2,2]))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.majorityElement([2,2,1,1,1,2,2]))
