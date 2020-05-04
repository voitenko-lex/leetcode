#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result = 0
        dict_nums = {}

        for item in nums:
            if item in dict_nums:
                dict_nums.pop(item)
            else:
                dict_nums[item] = 1
            print(dict_nums)
        # print(next(iter(dict_nums)))

        return next(iter(dict_nums))



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(1, self.sol.singleNumber([2,2,1]))

    def test_sample01(self):
        self.assertEqual(4, self.sol.singleNumber([4,1,2,1,2]))

if __name__ == '__main__':
    if False:
        unittest.main()
    else:
        sol = Solution()
        print(sol.singleNumber([2,2,1]))
