#!/usr/bin/env python
# -*- coding: utf-8 -*-
        
import unittest

def ToReverseListNode(source: str):
    nextv = None
    for i in source:
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
        result = str(self.val)
        pointer = self.next
        while pointer != None:
            result = result + " <- " + str(pointer.val)
            pointer = pointer.next
        return result

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curval = ListNode(0)
        result = curval
        i = 0

        while (curval.val > 0 or l1 or l2) and  i<10:
            i += 1
            # print(f"Iter {i}, {curval.val} + [{l1.val} + {l2.val}]")
            curval.next = ListNode(0)
            local_sum = curval.val
            if l1:
                local_sum += int(l1.val)
            if l2:
                local_sum += int(l2.val)

            curval.val = local_sum % 10
            curval.next.val = local_sum // 10
            lastval = curval
            curval = curval.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        else:
            lastval.next = None

        # print(f"result {result}")
        return result



        # nextval = 0
        # while pointer != None:
            
        #     curval = l1.val + l2.val + nextval
        #     nextval = curval//10
        #     curval = curval%10
        #     curnode = ListNode()
        #     l1 = l1.next
        #     l2 = l2.next


class TestStringMethods(unittest.TestCase):
    sol = Solution()

    def addTwoNumbersTest(self, val1, val2):
        test_val1 = ToReverseListNode(str(val1))
        test_val2 = ToReverseListNode(str(val2))
        test_result = ToReverseListNode(str(val1+val2))
        
        print("-----------\n{}\n + \n{} \n = \n{}".format(test_val1, test_val2, test_result))
        print("===========")
        print(self.sol.addTwoNumbers(test_val1, test_val2))
        
        self.assertEqual(str(self.sol.addTwoNumbers(test_val1, test_val2)), str(test_result))


        # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        # Output: 7 -> 0 -> 8
        # Explanation: 342 + 465 = 807.

    def test_sample00(self):
        self.addTwoNumbersTest(203, 308)

    def test_sample01(self):
        self.addTwoNumbersTest(202, 0)

    def test_sample03(self):
        self.addTwoNumbersTest(789, 333)

    def test_sample04(self):
        self.addTwoNumbersTest(2, 10)

if __name__ == '__main__':
    unittest.main()


