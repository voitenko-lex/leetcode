#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:
    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.

"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0

        for char in J:
            result += S.count(char)

        return result



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(3, self.sol.numJewelsInStones(J="aA", S="aAAbbbb"))

    def test_sample01(self):
        self.assertEqual(0, self.sol.numJewelsInStones(J="z", S="ZZ"))

if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.numJewelsInStones(J="aA", S="aAAbbbb"))
