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
    def longestPalindrome(self, s: str) -> str:
        """
        1616 ms / 13.8 MB
        """
        try:
            result_txt = s[0]
        except:
            result_txt = ""
        result_len = 1

        # print(f"{s}")
        

        for cur_pos, char in enumerate(s):
            nchars = s.count(char, cur_pos)
            # print(f"{cur_pos} {char} {nchars}")
            if nchars > 1:
                look_pos = cur_pos+1
                for _ in range(nchars-1):
                    look_pos = s.find(char, look_pos) + 1
                    # print(f" > {cur_pos} {look_pos} {s[cur_pos:look_pos]}=={s[cur_pos:look_pos][::-1]}={s[cur_pos:look_pos]==s[cur_pos:look_pos][::-1]}")
                    if (look_pos - cur_pos > result_len) and (s[cur_pos:look_pos]==s[cur_pos:look_pos][::-1]):
                        result_txt = s[cur_pos:look_pos]
                        result_len = len(result_txt)
                    #    print(f" >> {result_txt}")

        return result_txt

            
    
    # def longestPalindrome(self, s: str) -> str:
    #     """
    #     7312 ms / 12.9 MB
    #     """
    #     result_txt = ""

    #     for i in range(len(s)+1):
    #         for j in range(i):
    #             sample = s[j:i]
    #             if sample == sample[::-1]:
    #                 if len(result_txt) < len(sample):
    #                     result_txt = sample
        
    #     return result_txt

    
    # def longestPalindrome(self, s: str) -> str:
    #     """
    #     4808 ms / 13.6 MB
    #     """
    #     result_txt = ""

    #     for i in range(len(s)+1):
    #         for j in range(i):
    #             if (i-j) > len(result_txt):
    #                 sample = s[j:i]
    #                 if sample == sample[::-1]:
    #                     if len(result_txt) < len(sample):
    #                         result_txt = sample
        
    #     return result_txt


    # def longestPalindrome(self, s):
    #     pass

class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual("bab", self.sol.longestPalindrome("babad"))

    def test_sample01(self):
        self.assertEqual("bb", self.sol.longestPalindrome("cbbd"))

    def test_sample02(self):
        self.assertEqual("a", self.sol.longestPalindrome("a"))
    
    def test_sample03(self):
        self.assertEqual("", self.sol.longestPalindrome(""))

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        # print("12345"[-1:2])
        sol = Solution()
        print(sol.longestPalindrome("abcaac"))