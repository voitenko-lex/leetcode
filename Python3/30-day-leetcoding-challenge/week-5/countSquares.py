#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.



Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1

   Hide Hint #1
Create an additive table that counts the sum of elements of submatrix with the superior corner at (0,0).
   Hide Hint #2
Loop over all subsquares in O(n^3) and check if the sum make the whole array to be ones, if it checks then add 1 to the answer.
"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        len_y = len(matrix)
        len_x = len(matrix[0])

        add_matrix = [[0 for _ in range(len_x)] for _ in range(len_y)]


        for y in range(len_y):
            for x in range(len_x):
                if x==0 or y==0 or matrix[y][x] == 0:
                    add_matrix[y][x] = matrix[y][x]
                else:
                    add_matrix[y][x] = matrix[y][x] + min(add_matrix[y-1][x], add_matrix[y][x-1], add_matrix[y-1][x-1])
                result += add_matrix[y][x]

        # [print(row) for row in matrix]
        # print("-"*100)
        # [print(row) for row in add_matrix]
        return result



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(15, self.sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))

    def test_sample01(self):
        self.assertEqual(7, self.sol.countSquares([[1,0,1],[1,1,0],[1,1,0]]))

    # def test_sample02(self):
    #     self.assertEqual(False, self.sol.countSquares(root = [1,2,3,None,4], x = 2, y = 3))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))


