#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000

Example 4:
    Input: nums1 = [], nums2 = [1]
    Output: 1.00000

Example 5:
    Input: nums1 = [2], nums2 = []
    Output: 2.00000

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2
        com_len = len(nums1) + len(nums2)
        if com_len % 2 == 0:
            median_pos = int(com_len/2 - 1)
            # print(f"even, median_pos = {median_pos}")
            for _ in range(median_pos):
                self.pluck()
            return (self.pluck() + self.pluck())/2
        else:
            median_pos = int((com_len - 1)/2)
            # print(f"odd, median_pos = {median_pos}")
            # skip top elements
            for _ in range(median_pos):
                self.pluck()
            return float(self.pluck())        # result = 0
        # return median_pos

    def pluck(self):
        if len(self.nums1) < 1:
            return self.nums2.pop(0)
        elif len(self.nums2) < 1:
            return self.nums1.pop(0)
        else:
            if self.nums1[0] <= self.nums2[0]:
                return self.nums1.pop(0)
            else:
                return self.nums2.pop(0)


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])
        test_output = 2.00000
        self.assertEqual(test_output, test_input)

    def test_sample01(self):
        test_input = self.sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
        test_output = 2.50000
        self.assertEqual(test_output, test_input)

    def test_sample02(self):
        test_input = self.sol.findMedianSortedArrays(nums1 = [0,0], nums2 = [0,0])
        test_output = 0.00000
        self.assertEqual(test_output, test_input)

    def test_sample03(self):
        test_input = self.sol.findMedianSortedArrays(nums1 = [], nums2 = [1])
        test_output = 1.00000
        self.assertEqual(test_output, test_input)

    def test_sample04(self):
        test_input = self.sol.findMedianSortedArrays(nums1 = [2], nums2 = [])
        test_output = 2.00000
        self.assertEqual(test_output, test_input)


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.findMedianSortedArrays(nums1 = [1,1,5], nums2 = [2]))



