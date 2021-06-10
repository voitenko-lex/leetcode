#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### 10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
    Input: s = "aab", p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
    Input: s = "mississippi", p = "mis*is*p*."
    Output: false


Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(f"String: {s}\nPattern: {p}")

        pos_s = 0
        for pos_p in range(len(p)):
            print(f"Current pattern: {pos_p} {p[pos_p]}, string: {s[pos_s:]}")
            if p[pos_p] == s[pos_s]:
                pos_s +=1
            else:
                return False

        return pos_s == len(s)


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.isMatch(s = "aa", p = "a")
        test_output = False
        self.assertEqual(test_output, test_input)

    def test_sample01(self):
        test_input = self.sol.isMatch(s = "aa", p = "a*")
        test_output = True
        self.assertEqual(test_output, test_input)

    def test_sample02(self):
        test_input = self.sol.isMatch(s = "ab", p = ".*")
        test_output = True
        self.assertEqual(test_output, test_input)

    def test_sample03(self):
        test_input = self.sol.isMatch(s = "aab", p = "c*a*b")
        test_output = True
        self.assertEqual(test_output, test_input)

    def test_sample04(self):
        test_input = self.sol.isMatch(s = "mississippi", p = "mis*is*p*.")
        test_output = False
        self.assertEqual(test_output, test_input)


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.isMatch(s = "abcd", p = "abcd"))



