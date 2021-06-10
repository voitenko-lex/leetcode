#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
    # def removeKdigits1(self, num: str, k: int) -> str:
    #     result = num
    #     if k>0:
    #         min_num = int(num)
    #         for i in range(len(num)):
    #             test = num[:i] + num[i+1:]
    #             if test:
    #                 test_num = int(test)
    #             else:
    #                 test_num = 0
    #             if test_num < min_num: min_num = test_num
    #         result = str(min_num)
    #         result = self.removeKdigits(result, k-1)
    #     return result

    # def removeKdigits2(self, num: str, k: int) -> str:
    #     if len(num) <= k: return "0"
    #     i = 1
    #     while i < len(num) and k > 0:
    #         if (num[i-1]) > (num[i]):
    #             num = num[:i-1] + num[i:]
    #             k -= 1
    #             if i>1: i -= 1
    #         else:
    #             i += 1

    #     if k>0:
    #         num = num[:-k]

    #     if num:
    #         num = str(int(num))
    #     else:
    #         num = "0"

    #     return num

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: return "0"
        stack = []
        charsToRemove = k
        for c in num:
            while stack and stack[-1] > c and charsToRemove > 0:
                stack.pop()
                charsToRemove -= 1

            stack.append(c)

        while charsToRemove > 0:
            stack.pop()
            charsToRemove -= 1

        rslt = ''.join(stack).lstrip('0')
        return rslt if rslt else '0'


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual("1219", self.sol.removeKdigits(num = "1432219", k = 3))

    def test_sample01(self):
        self.assertEqual("200", self.sol.removeKdigits(num = "10200", k = 1))

    def test_sample02(self):
        self.assertEqual("0", self.sol.removeKdigits(num = "10", k = 2))

    def test_sample03(self):
        self.assertEqual("0", self.sol.removeKdigits(num = "9", k = 1))

    def test_sample04(self):
        self.assertEqual("0", self.sol.removeKdigits(num = "1234567890", k = 9))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        # print(sol.removeKdigits(num = "9964143637881536115347130215819342018286368478941148499497648482711459533461004", k = 70))
        print(sol.removeKdigits(num = "1234567890", k = 9))
        # print("123"[:0])


