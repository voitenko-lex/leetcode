#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Flood Fill

An image is represented by a 2-D array of integers,
each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column)
of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color as the starting pixel), and so on.
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

    Input:
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation:
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.

Note:
    The length of image and image[0] will be in the range [1, 50].
    The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

import unittest
from typing import List, Set, Tuple, Dict

import math

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        [print(row) for row in image]
        buffer = image[sr][sc]
        image[sr][sc] = newColor
        if sr+1 < len(image):
            if image[sr+1][sc] == buffer:
                image = self.floodFill(image, sr+1, sc, newColor)
        if sr-1 >= 0:
            if image[sr-1][sc] == buffer:
                image = self.floodFill(image, sr-1, sc, newColor)
        if sc+1 < len(image[sr]):
            if image[sr][sc+1] == buffer:
                image = self.floodFill(image, sr, sc+1, newColor)
        if sc-1 >= 0:
            if image[sr][sc-1] == buffer:
                image = self.floodFill(image, sr, sc-1, newColor)

        return image


        # while True:



class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual([[2,2,2],[2,2,0],[2,0,1]], self.sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))

    # def test_sample01(self):
    #     self.assertEqual(False, self.sol.floodFill([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.floodFill(image = [[0,0,0],[0,1,1]], sr = 1, sc = 1, newColor = 1))



