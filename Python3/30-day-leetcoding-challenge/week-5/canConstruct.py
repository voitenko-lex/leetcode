#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Number Complement

Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. 
So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. 
So you need to output 0.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

import unittest
from typing import List, Set, Tuple, Dict

import math

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0: return 1
        base = 0
        for _ in range(num.bit_length()):
            base = base << 1 
            base += 1
        
        print(f"\n\n")
        print(f"len    = {num:b} ({num.bit_length()})")
        print(f"base    = {base:b} ({base}) {base.bit_length()}")
        print(f"result   = {base ^ num:b} ({base ^ num})")

        return base ^ num

    # def findComplement(self, num: int) -> int:
    #     if num == 0: return 1
    #     log = math.log2(num)
    #     degree = math.ceil(log)
    #     if degree == log: degree += 1
    #     if degree < 1: degree = 1
    #     base = 2**(degree) - 1
    #     print(f"\n\n")
    #     print(f"num    = {num:b} ({num})")
    #     print(f"base   = {base:b} ({base})")
    #     print(f"result = {num^base:b} ({num^base})")
    #     return num^base

    # def findComplement(self, num: int) -> int:
    #     if num == 0: return 1
    #     t = num
    #     res = 0
    #     while t > 0:
    #         t = t >> 1
    #         res = res << 1
    #         res += 1
    #     return res ^ num


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(1, self.sol.findComplement(0))

    def test_sample01(self):
        self.assertEqual(0, self.sol.findComplement(1))

    def test_sample02(self):
        self.assertEqual(1, self.sol.findComplement(2))

    def test_sample03(self):
        self.assertEqual(0, self.sol.findComplement(3))

    def test_sample04(self):
        self.assertEqual(3, self.sol.findComplement(4))

    def test_sample05(self):
        self.assertEqual(2, self.sol.findComplement(5))

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        print(sol.findComplement(3))



