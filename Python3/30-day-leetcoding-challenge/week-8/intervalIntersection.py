#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty,
or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


Example 1:
    Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

Note:
    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

"""

import unittest
from typing import List, Set, Tuple, Dict

# import collections

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B: return []

        result = []
        pos_a = 0
        pos_b = 0
        start_pos = 0
        end_pos = 0

        while True:
            print(f"A[{pos_a}] = {A[pos_a]}, B[{pos_b}] = {B[pos_b]}")

            start_pos = max(A[pos_a][0], B[pos_b][0])
            end_pos = min(A[pos_a][1], B[pos_b][1])

            if start_pos <= end_pos:
                result.append([start_pos, end_pos])
                print(f"result = {[start_pos, end_pos]}")

            if pos_b + 1 < len(B) and A[pos_a][1] >= B[pos_b + 1][0]:
                pos_b += 1
            elif pos_a + 1 < len(A) and A[pos_a + 1][0] <= B[pos_b][1]:
                pos_a += 1
            elif pos_b + 1 < len(B) and pos_a + 1 < len(A):
                pos_a += 1
                pos_b += 1
            else:
                break
        return result



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(   [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]],
                            self.sol.intervalIntersection(  A = [[0,2],[5,10],[13,23],[24,25]],
                                                            B = [[1,5],[8,12],[15,24],[25,26]]))

    def test_sample01(self):
        self.assertEqual(   [[16,16]],
                            self.sol.intervalIntersection(  A = [[14,16]],
                                                            B = [[7,13],[16,20]]))

    def test_sample02(self):
        self.assertEqual(   [[10,11],[19,19]],
                            self.sol.intervalIntersection(  A = [[10,12],[18,19]],
                                                            B = [[1,6],[8,11],[13,17],[19,20]]))

if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.intervalIntersection(      A = [[10,12],[18,19]],
                                                            B = [[1,6],[8,11],[13,17],[19,20]]))
