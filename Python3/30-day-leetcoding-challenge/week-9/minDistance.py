#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cur_row = [num for num in range(len(word1) + 1)]
        prev_row = []

        # print(cur_row)
        for word2_pos in range(1, len(word2)+1):
            prev_row = cur_row
            cur_row = [0 for x in range(len(word1) + 1) ]
            for word1_pos in range(len(word1) + 1):
                if word1_pos == 0: 
                    cur_row[word1_pos] = word2_pos
                else:
                    if word1[word1_pos - 1] == word2[word2_pos - 1]:
                        cur_row[word1_pos] = prev_row[word1_pos - 1]
                    else:
                        cur_row[word1_pos] = 1 + min(   cur_row[word1_pos - 1], 
                                                        prev_row[word1_pos],
                                                        prev_row[word1_pos - 1])

            # print(cur_row)
        
        return cur_row[len(word1)]
            
    # def minDistance(self, word1: str, word2: str) -> int:
    #     @functools.lru_cache(None)
    #     def dfs(i=0, j=0):
    #         if i == len(word1): return len(word2) - j
    #         if j == len(word2): return len(word1) - i
    #         if word1[i] == word2[j]: return dfs(i + 1, j + 1)
    #         else: return 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
    #     return dfs()


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.minDistance(word1 = "horse", word2 = "ros")
        test_output = 3
        self.assertEqual(test_output, test_input)

    def test_sample01(self):
        test_input = self.sol.minDistance(word1 = "intention", word2 = "execution")
        test_output = 5
        self.assertEqual(test_output, test_input)


if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        # print(sol.minDistance(word1 = "horse", word2 = "ros"))
        print(sol.minDistance(word1 = "abcdef", word2 = "azced"))



