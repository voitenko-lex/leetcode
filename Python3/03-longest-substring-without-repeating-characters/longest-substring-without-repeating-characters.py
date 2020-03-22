#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

"""

import unittest

class Solution:
    def lengthOfLongestSubstring(self, s):
        spos = 0
        epos = 0
        result = 0

        for pos, char in enumerate(s):
            print("{} {} in s[{};{}] {} = {}".format(pos, char, spos, epos, s[spos:epos+1], char in s[spos:epos]))
            if char in s[spos:epos+1]:
                if (epos-spos) > result:
                    result = (epos-spos) + 1

                spos = pos
                epos = pos
            else:
                epos = pos

        return result


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(3, self.sol.lengthOfLongestSubstring("abcabcbb"))

    def test_sample01(self):
        self.assertEqual(1, self.sol.lengthOfLongestSubstring("bbbbb"))

    def test_sample02(self):
        self.assertEqual(3, self.sol.lengthOfLongestSubstring("pwwkew"))

    def test_sample03(self):
        self.assertEqual(1, self.sol.lengthOfLongestSubstring(" "))

    def test_sample04(self):
        self.assertEqual(0, self.sol.lengthOfLongestSubstring(""))

if __name__ == '__main__':
    if False:
        unittest.main()
    else:
        sol = Solution()
        print(sol.lengthOfLongestSubstring("pwwkeww"))