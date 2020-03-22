"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""

import unittest

class Solution:
    # def reverse(self, x: int) -> int:
    def reverse(self, x):
        pass

class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(321, self.sol.reverse(123))

    def test_sample01(self):
        self.assertEqual(-321, self.sol.reverse(-123))

    def test_sample02(self):
        self.assertEqual(21, self.sol.reverse(120))

if __name__ == '__main__':
    if False:
        unittest.main()
    else:
        pass