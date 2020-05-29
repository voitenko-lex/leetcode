#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b 
into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: 
Output: 
Explanation: group1 [1,4], group2 [2,3]

Example 2:

Input: 
Output: 

Example 3:

Input: 
Output: 

 

Constraints:

    1 <= N <= 2000
    0 <= dislikes.length <= 10000
    dislikes[i].length == 2
    1 <= dislikes[i][j] <= N
    dislikes[i][0] < dislikes[i][1]
    There does not exist i != j for which dislikes[i] == dislikes[j].
"""

import unittest
from typing import List, Set, Tuple, Dict
import collections

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # if not dislikes: return True
        
        def dfs(i):
            open_list = [i]
            colors[i] = 1
            while open_list:
                i = open_list.pop()
                for v in connections[i]:
                    if v in colors:
                        if colors[v] != -colors[i]: return False
                    else:
                        colors[v] = -colors[i]
                        open_list.append(v)

            return True

        connections = collections.defaultdict(list)
        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)
        
        colors = {}
        for i in range(1, N+1):
            if i not in colors and not dfs(i): return False
        return True  


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.possibleBipartition(N = 4, dislikes = [[1,2],[1,3],[2,4]])
        test_output = True
        self.assertEqual(test_output, test_input)

    def test_sample01(self):
        test_input = self.sol.possibleBipartition(N = 3, dislikes = [[1,2],[1,3],[2,3]])
        test_output = False
        self.assertEqual(test_output, test_input)

    def test_sample02(self):
        test_input = self.sol.possibleBipartition(N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]])
        test_output = False
        self.assertEqual(test_output, test_input)




if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        print(sol.possibleBipartition(N = 4, dislikes = [[1,2],[1,3],[2,4]]))



