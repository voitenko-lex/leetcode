#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's2 permutations is the substring of the second string.


Example 1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False

Note:
    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

   Hint #1  
        Obviously, brute force will result in TLE. Think of something else.
   Hint #2  
        How will you check whether one string is a permutation of another string?
   Hint #3  
        One way is to sort the string and then compare. But, Is there a better way?
   Hint #4  
        If one string is a permutation of another string then they must one common metric. What is that?
   Hint #5  
        Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
   Hint #6  
        What about hash table? An array of size 26?
"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        FIRST_CHAR = 97
        LAST_CHAR = FIRST_CHAR + 26
        result = []

        search_pool = {chr(i): 0 for i in range(FIRST_CHAR,LAST_CHAR)}
        match_pool = search_pool.copy()

        for char in s1:
            match_pool[char] += 1
        
        for char in s2[:len(s1)]:
            search_pool[char] += 1

        start_pos = 0
        while True:
            if search_pool == match_pool:
                return True
            if start_pos < len(s2)-len(s1):
                search_pool[s2[start_pos+len(s1)]] += 1
                search_pool[s2[start_pos]] -= 1
                start_pos += 1
            else:
                break
        return False


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(True, self.sol.checkInclusion(s2="cbaebabacd", s1="abc"))

    def test_sample01(self):
        self.assertEqual(True, self.sol.checkInclusion(s2="abab", s1="ab"))

    def test_sample02(self):
        self.assertEqual(True, self.sol.checkInclusion(s2="baa", s1="aa"))

    def test_sample03(self):
        self.assertEqual(True, self.sol.checkInclusion(s1 = "ab", s2 = "eidbaooo"))

    def test_sample04(self):
        self.assertEqual(False, self.sol.checkInclusion(s1= "ab", s2 = "eidboaoo"))

        

    

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        # print(sol.checkInclusion(s2="cbaebabacd", s1="abc"))
        # print(sol.checkInclusion(s2="abab", s1="ab"))
        print(sol.checkInclusion(s2="baa", s1="aa"))


