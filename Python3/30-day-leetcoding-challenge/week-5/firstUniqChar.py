#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

"""

import unittest
from typing import List, Set, Tuple, Dict

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = -1
        freq = collections.Counter(s)
        for el in freq:
            if freq[el]==1:
                return s.index(el)

        return result



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(0, self.sol.firstUniqChar("leetcode"))

    def test_sample01(self):
        self.assertEqual(0, self.sol.firstUniqChar("loveleetcode"))

    def test_sample02(self):
        self.assertEqual(-1, self.sol.firstUniqChar("dodo"))

if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.firstUniqChar("afgddag"))
