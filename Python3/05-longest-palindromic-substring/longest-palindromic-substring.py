"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""
import unittest

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    
    # def longestPalindrome(self, s):
        # """
        # 7312 ms / 12.9 MB
        # """
        # result_txt = ""

        # for i in range(len(s)+1):
        #     for j in range(i):
        #         sample = s[j:i]
        #         if sample == sample[::-1]:
        #             if len(result_txt) < len(sample):
        #                 result_txt = sample
        
        # return result_txt

    def longestPalindrome(self, s):
        pass

class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual("bab", self.sol.longestPalindrome("babad"))

    def test_sample01(self):
        self.assertEqual("bb", self.sol.longestPalindrome("cbbd"))

    def test_sample02(self):
        self.assertEqual("a", self.sol.longestPalindrome("a"))

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        # print("12345"[-1:2])
        sol = Solution()
        print(sol.longestPalindrome("a"))