#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
## Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    - The town judge trusts nobody.
    - Everybody (except for the town judge) trusts the town judge.
    - There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Note:

    1 <= N <= 1000
    trust.length <= 10000
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N


Example 1:
    Input: N = 2, trust = [[1,2]]
    Output: 2

Example 2:
    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

Example 3:
    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Example 4:
    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

Example 5:
    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3
"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        scores = {x:0 for x in range(1, 1+N)}
        for pair in trust:
            # scores[pair[0]] -= 1
            try:
                scores.pop(pair[0])
            except KeyError:
                pass
            scores[pair[1]] += 1

        print(f"\n {scores}")
        for el in scores:
            if scores[el] == N-1: return el

        return -1


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(2, self.sol.findJudge(N=2, trust=[[1,2]]))

    def test_sample01(self):
        self.assertEqual(3, self.sol.findJudge(N=3, trust=[[1,3],[2,3]]))

    def test_sample02(self):
        self.assertEqual(-1, self.sol.findJudge(N=3, trust=[[1,3],[2,3],[3,1]]))

    def test_sample03(self):
        self.assertEqual(-1, self.sol.findJudge(N=3, trust=[[1,2],[2,3]]))

    def test_sample04(self):
        self.assertEqual(3, self.sol.findJudge(N=4, trust=[[1,3],[1,4],[2,3],[2,4],[4,3]]))

    def test_sample05(self):
        self.assertEqual(1, self.sol.findJudge(N=1, trust=[]))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.findJudge(N=1, trust=[]))