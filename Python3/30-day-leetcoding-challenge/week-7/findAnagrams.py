#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p
will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     result = []
    #     search_indexes = {char: set() for char in p}

    #     for pos, char in enumerate(s):
    #         if char in search_indexes.keys():
    #             search_indexes[char].add(pos)

    #     print(f"search_indexes = {search_indexes}")

    #     start_pos = 0
    #     while start_pos <= (len(s) - len(p)):
    #         search_pool = set(range(start_pos, start_pos+len(p)))
    #         print(f"start_pos={start_pos}, end_pos={start_pos+len(p)}, search_pool = {search_pool}")
    #         intersections = 0
    #         for char in search_indexes:
    #             if search_pool.intersection(search_indexes[char]):
    #                 intersections += 1
    #         print(f"intersections = {intersections}")
    #         if intersections == len(p):
    #             print(f"FOUND!! = {start_pos}")
    #             result.append(start_pos)
    #         start_pos += 1

    #     return result


    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     print(f"findAnagrams(self, {s}, {p})")
    #     result = []

    #     start_pos = 0
    #     while start_pos <= (len(s) - len(p)):
    #         search_str = s[start_pos:start_pos+len(p)]
    #         match_str = p
    #         for char in match_str:
    #             search_str = search_str.replace(char, "", 1)
    #         if not len(search_str):
    #             result.append(start_pos)
    #         start_pos += 1

    #     return result

    def findAnagrams(self, s: str, p: str) -> List[int]:
        FIRST_CHAR = 97
        LAST_CHAR = FIRST_CHAR + 26
        result = []

        search_pool = {chr(i): 0 for i in range(FIRST_CHAR,LAST_CHAR)}
        match_pool = search_pool.copy()

        for char in p:
            match_pool[char] += 1

        for char in s[:len(p)]:
            search_pool[char] += 1

        start_pos = 0
        while True:
            if search_pool == match_pool:
                result.append(start_pos)
            if start_pos < len(s)-len(p):
                search_pool[s[start_pos+len(p)]] += 1
                search_pool[s[start_pos]] -= 1
                start_pos += 1
            else:
                break


        return result


    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     left=right=0
    #     match_pool = {i:0 for i in p}
    #     for i in p:
    #         match_pool[i] += 1
    #     len_s = len(s)
    #     len_match_pool = len(match_pool)
    #     result = []
    #     while right < len_s:
    #         if s[right] in match_pool:
    #             match_pool[s[right]] -= 1
    #             if match_pool[s[right]] == 0:
    #                 len_match_pool -= 1
    #         right += 1
    #         while not len_match_pool:
    #             if right - left == len(p):
    #                 result.append(left)
    #             if s[left] in match_pool:
    #                 match_pool[s[left]] += 1
    #                 if  match_pool[s[left]] == 1: len_match_pool += 1

    #             left += 1

    #     return result





class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual([0,6], self.sol.findAnagrams(s="cbaebabacd", p="abc"))

    def test_sample01(self):
        self.assertEqual([0, 1, 2], self.sol.findAnagrams(s="abab", p="ab"))

    def test_sample02(self):
        self.assertEqual([1], self.sol.findAnagrams(s="baa", p="aa"))





if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        # print(sol.findAnagrams(s="cbaebabacd", p="abc"))
        # print(sol.findAnagrams(s="abab", p="ab"))
        print(sol.findAnagrams(s="baa", p="aa"))


