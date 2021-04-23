#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### 9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true


Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
 
"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revertedNumber, src = 0, x
        while src > 0:
            src, num = divmod(src, 10)
            revertedNumber = revertedNumber*10 + num

        print(revertedNumber, x)
        return revertedNumber == x


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.isPalindrome(121)
        test_output = True
        self.assertEqual(test_output, test_input)

    def test_sample01(self):
        test_input = self.sol.isPalindrome(-121)
        test_output = False
        self.assertEqual(test_output, test_input)

    def test_sample02(self):
        test_input = self.sol.isPalindrome(10)
        test_output = False
        self.assertEqual(test_output, test_input)

    def test_sample03(self):
        test_input = self.sol.isPalindrome(-101)
        test_output = False
        self.assertEqual(test_output, test_input)


if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        print(sol.isPalindrome(123202))



