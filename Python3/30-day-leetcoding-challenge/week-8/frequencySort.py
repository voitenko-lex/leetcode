#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input: "tree"
Output: "eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: "cccaaa"
Output: "cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: "Aabb"
Output: "bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

import unittest
from typing import List, Set, Tuple, Dict

import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        sorted_freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        # print(sorted_freq)
        result = "".join([k*sorted_freq[k] for k in sorted_freq])
        return result



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual("eetr", self.sol.frequencySort("tree"))

    def test_sample01(self):
        self.assertEqual("cccaaa", self.sol.frequencySort("cccaaa"))

    def test_sample02(self):
        self.assertEqual("bbAa", self.sol.frequencySort("Aabb"))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.frequencySort("Aaaabbbddddd"))


