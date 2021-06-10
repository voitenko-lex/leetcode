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
32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""

import unittest

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        k = 1 if x >= 0 else -1
        x *= k
        while x >= 10:
            a = x % 10
            result = result * 10 + a
            x = x // 10
            # print(f"x={x} result={result}" )

        result = k*(result * 10 + x)
        if abs(result) > 2**31: result = 0
        return result




class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(321, self.sol.reverse(123))

    def test_sample01(self):
        self.assertEqual(-321, self.sol.reverse(-123))

    def test_sample02(self):
        self.assertEqual(21, self.sol.reverse(120))

    def test_sample03(self):
        self.assertEqual(0, self.sol.reverse(123456789))

if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.reverse(-1201))
        # sol.reverse(12)
        # x = -12
        # print(f"x={x} |x|={abs(x)} {x // 10} {abs(x) // 10}")