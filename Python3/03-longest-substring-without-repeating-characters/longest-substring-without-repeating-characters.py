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
        epos = -1
        result = 0
        buffer = {}

        for pos, char in enumerate(s):
            epos += 1
            # print(f"{pos} {char} in s[{spos};{epos}] {s[spos:epos+1]} {buffer}")
            if (char in buffer) and (buffer[char] >= spos):
                spos = buffer[char] + 1
            buffer[char] = pos

            if (epos - spos + 1) > result:
                result = (epos - spos + 1)

            # print(f"result = {result}")

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
    if True:
        unittest.main()
    else:
        sol = Solution()
        print(sol.lengthOfLongestSubstring("pwwkeww"))