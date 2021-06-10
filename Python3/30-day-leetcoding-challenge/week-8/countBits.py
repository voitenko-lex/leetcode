#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

   Hide Hint #1
You should make use of what you have produced already.
   Hide Hint #2
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
   Hide Hint #3
Or does the odd/even status of the number help you in calculating the number of 1s?
"""

import unittest
from typing import List, Set, Tuple, Dict
import collections

def bitsoncount(x):
    return bin(x).count('1')

class Solution:
    # def countBits(self, num: int) -> List[int]:
    #     result = []
    #     for x in range(num+1):
    #         result.append(bin(x).count('1'))

    #     return result

    def countBits(self, num: int) -> List[int]:
        result = [0] * (num+1)
        for x in range(1, num+1):
            result[x] = (result[x>>1] + x%2)
        return result


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual([0], self.sol.countBits(0))

    def test_sample01(self):
        self.assertEqual([0,1,1], self.sol.countBits(2))

    def test_sample02(self):
        self.assertEqual([0,1,1,2,1,2], self.sol.countBits(5))

if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.countBits(20))



