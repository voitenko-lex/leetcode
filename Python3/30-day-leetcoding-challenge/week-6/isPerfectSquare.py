#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true

Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""

import unittest
from typing import List, Set, Tuple, Dict

import math

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Ax + By + C = 0
        # (y1 - y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0

        A = coordinates[0][1] - coordinates[1][1]
        B = coordinates[1][0] - coordinates[0][0]
        C = coordinates[0][0] * coordinates[1][1] - coordinates[1][0] * coordinates[0][1]

        print(f"{A}x + {B}y + {C} = 0")

        for i in range(2,len(coordinates)):
            if (A*coordinates[i][0] + B*coordinates[i][1] + C) != 0:
                return False
        return True


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(True, self.sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))

    def test_sample01(self):
        self.assertEqual(False, self.sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))



