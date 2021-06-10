#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:
    Input: root = [1,2,3,None,4,None,5], x = 5, y = 4
    Output: true

Example 3:
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

Note:
    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.

"""

import unittest
from typing import List, Set, Tuple, Dict

import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print(self.val)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

class Solution:
    def getBTschem(self, bt: TreeNode, depth: int = 0, prnt: int = 0, bt_dict: Dict  = {}) -> Dict:
        """
        Inputs:
            bt - pointer on current position in binary tree
            depth - current depth in binary tree
            prnt - value of parent node of binary tree
            bt_dict - dictionary of levels for each value in binary tree
        Outputs:
            bt_dict - dictionary of levels for each value in binary tree
        """
        bt_dict[bt.val] = [depth, prnt]

        if bt.left:
            bt_dict = self.getBTschem(bt.left, depth+1, bt.val, bt_dict)
        if bt.right:
            bt_dict = self.getBTschem(bt.right, depth+1, bt.val, bt_dict)

        return bt_dict


    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dict_lvl = self.getBTschem(root)
        print(dict_lvl)
        if (dict_lvl[x][0] == dict_lvl[y][0]) and (dict_lvl[x][1] != dict_lvl[y][1]): return True
        return False






class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(False, self.sol.isCousins(root = [1,2,3,4], x = 4, y = 3))

    def test_sample01(self):
        self.assertEqual(True, self.sol.isCousins(root = [1,2,3,None,4,None,5], x = 5, y = 4))

    def test_sample02(self):
        self.assertEqual(False, self.sol.isCousins(root = [1,2,3,None,4], x = 2, y = 3))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        tree = TreeNode(    1,
                            TreeNode(   2,
                                        TreeNode(   4,
                                                    None,
                                                    None),
                                        None),
                            TreeNode(   3,
                                        None,
                                        None))
        # tree.PrintTree()
        print(sol.isCousins(root = tree, x = 3, y = 4))



