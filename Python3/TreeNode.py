#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
## Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
    Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



Constraints:

    The number of elements of the BST is between 1 to 10^4.
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

   Hide Hint #1
Try to utilize the property of a BST.
   Hide Hint #2
Try in-order traversal. (Credits to @chan13)
   Hide Hint #3
What if you could modify the BST node's structure?
   Hide Hint #4
The optimal runtime complexity is O(height of BST).
"""

import unittest
from typing import List, Set, Tuple, Dict

# import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_depth(self, depth = 0):
        depth += 1
        depth_left = 0
        depth_right = 0
        if self.left:
            depth_left = self.left.get_depth()
        if self.right:
            depth_right = self.right.get_depth()

        return depth + max(depth_left, depth_right)

    def to_list(self, tree_list=None, n=1):
        if not tree_list:
            tree_list = [None for _ in range(2 ** self.get_depth())]
        tree_list[n-1] = self.val
        if self.left:
            tree_list = self.left.to_list(tree_list, 2*(n))
        if self.right:
            tree_list = self.right.to_list(tree_list, 2*(n)+1)

        return tree_list

    def to_set(self, tree_set=set()):
        tree_set.add(self.val)
        if self.left:
            tree_set = self.left.to_set(tree_set)
        if self.right:
            tree_set = self.right.to_set(tree_set)

        return tree_set

    def __str__(self):
        result = ""
        tree_list = self.to_list()
        tree_depth = self.get_depth() # The log() will be faster, but this will require the import of math
        cur_depth = 1
        for num, val in enumerate(tree_list):
            num += 1
            if num >= 2**cur_depth:
                cur_depth += 1
                result += "\n\n"
            result += "\t" * (tree_depth - cur_depth + 1)
            if val:
                result += str(val)
            else:
                result += "\t"

        return result


    @staticmethod
    def make_TreeNode(iterable):
        list_nodes = []
        for num, val in enumerate(iterable):
            new_node = TreeNode(val)
            list_nodes.append(new_node)
            num += 1
            if num > 1:
                root_node = num // 2
                if num % 2 == 0:
                    list_nodes[root_node-1].left = new_node
                else:
                    list_nodes[root_node-1].right = new_node

        return list_nodes[0]




class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        tree_list = list(root.to_set())
        print(tree_list)
        return tree_list[k-1]




class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(1, self.sol.kthSmallest(root = TreeNode.make_TreeNode([3,1,4,None,2]), k = 1))

    def test_sample01(self):
        self.assertEqual(3, self.sol.kthSmallest(root = TreeNode.make_TreeNode([5,3,6,2,4,None,None,1]), k = 3))

    # def test_sample02(self):
    #     self.assertEqual(False, self.sol.kthSmallest(root = [1,2,3,None,4], x = 2, y = 3))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        tree = TreeNode.make_TreeNode([5,3,6,2,4,None,None,1])
        # tree = TreeNode.make_TreeNode([1,2,3,4,5,6,7,8,9])
        # tree.PrintTree()
        # print(tree)
        print()
        # sol = Solution()
        # tree = TreeNode(    1,
        #                     TreeNode(   2,
        #                                 TreeNode(   4,
        #                                             None,
        #                                             None),
        #                                 None),
        #                     TreeNode(   3,
        #                                 None,
        #                                 None))
        # # tree.PrintTree()
        # print(sol.isCousins(root = tree, x = 3, y = 4))



