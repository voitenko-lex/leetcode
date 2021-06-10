#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
"""

import unittest
from typing import List, Set, Tuple, Dict

def toListNode(source):
    last_node = None
    first_node = None

    for i in source:
        node = ListNode(i)
        if not first_node: first_node = node
        if last_node: last_node.next = node
        last_node = node

    return first_node

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = str(self.val)
        pointer = self.next
        while pointer != None:
            result = result + " -> " + str(pointer.val)
            pointer = pointer.next
        return result


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        pointer = head
        odd_last = None
        even_first = None
        even_last = None
        is_odd = True

        while pointer != None:
            if is_odd:
                if odd_last: odd_last.next = pointer
                odd_last = pointer
            else:
                if not even_first: even_first = pointer
                if even_last: even_last.next = pointer
                even_last = pointer

            pointer = pointer.next
            is_odd = not is_odd

        if odd_last: odd_last.next = even_first
        if even_last: even_last.next = None

        return head

class TestMethods(unittest.TestCase):
    sol = Solution()

    def oddEvenListTest(self, check, test):
        check_node = toListNode(check)
        test_node = toListNode(test)
        self.assertEqual(str(check_node), str(self.sol.oddEvenList(test_node)))

    def test_sample00(self):
        self.oddEvenListTest([1,3,5,2,4], [1,2,3,4,5])

    def test_sample01(self):
        self.oddEvenListTest([], [])

    def test_sample02(self):
        self.oddEvenListTest([1], [1])


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        test_node = toListNode([1,2,3,4,5])
        print(sol.oddEvenList(test_node))


