#!/usr/bin/env python
# -*- coding: utf-8 -*-
        
import unittest

def ToReverseListNode(source: str):
    nextv = None
    for i in source[::-1]:
        node = ListNode(i)
        node.next = nextv
        nextv = node
    
    return nextv


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = self.val
        pointer = self.next
        while pointer != None:
            result = result + " <- " + pointer.val
            pointer = pointer.next
        return result

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

class TestStringMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input_nums = [2, 7, 11, 15]
        test_input_target = 9
        test_output = [0, 1]
        # self.assertEqual(self.sol.twoSum(test_input_nums, test_input_target), test_output)

    def test_sample01(self):
        test_input_nums = [3,2,4]
        test_input_target = 6
        test_output = [1, 2]
        # self.assertEqual(self.sol.twoSum(test_input_nums, test_input_target), test_output)0

if __name__ == '__main__':
    # unittest.main()
    testv = ToReverseListNode("908")
    print(testv)

