#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Given an arbitrary ransom note string and another string containing letters from all the magazines, 
 write a function that will return true if the ransom note can be constructed from the magazines ; 
 otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # result = 0

        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, "", 1)
            else:
                return False
        
        return True



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(False, self.sol.canConstruct("a", "b"))

    def test_sample01(self):
        self.assertEqual(False, self.sol.canConstruct("aa", "ab"))

    def test_sample02(self):
        self.assertEqual(True, self.sol.canConstruct("aa", "aab"))

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        print(sol.canConstruct("aa", "aab"))
