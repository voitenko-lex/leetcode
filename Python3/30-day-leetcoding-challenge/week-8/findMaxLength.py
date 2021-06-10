#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

import unittest
from typing import List, Set, Tuple, Dict
import collections

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        level = 0
        counts = {level: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                level -= 1
            else:
                level += 1

            if level in counts:
                result = max(result, i - counts[level])
            else:
                counts[level] = i

        return result


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = [0,1]
        test_output = 2
        self.assertEqual(test_output, self.sol.findMaxLength(test_input))


    def test_sample01(self):
        test_input = [0,1,0]
        test_output = 2
        self.assertEqual(test_output, self.sol.findMaxLength(test_input))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.findMaxLength(20))



