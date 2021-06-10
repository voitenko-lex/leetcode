#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
## Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left,
then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary
search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.


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
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root_note = TreeNode(preorder.pop(0))

        while preorder:
            new_note = TreeNode(preorder.pop(0))
            current_node = root_note

            while True:
                if new_note.val > current_node.val:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_note
                        break
                elif new_note.val < current_node.val:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_note
                        break
                else:
                    raise ValueError

        return root_note





class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(1, self.sol.bstFromPreorder([8,5,1,7,10,12]))


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        # tree = TreeNode.make_TreeNode([8,5,1,7,10,12])
        # print(tree)
        print(sol.bstFromPreorder([8,5,1,7,10,12]))


