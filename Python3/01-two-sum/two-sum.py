#!/usr/bin/env python
# -*- coding: utf-8 -*-
        
import unittest

class Solution:
#   First Solution  
    def twoSum(self, nums, target):
        tnums = tuple(nums)
        for first_el, first_el_val in enumerate(tnums):
            for second_el, second_el_val in enumerate(tnums[first_el+1:]):
                if first_el_val + second_el_val == target:
                    return [first_el, first_el + 1 + second_el]
    
#   Second Solution 
    # def twoSum(self, nums, target):
    #     pass


class TestStringMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input_nums = [2, 7, 11, 15]
        test_input_target = 9
        test_output = [0, 1]
        self.assertEqual(self.sol.twoSum(test_input_nums, test_input_target), test_output)

if __name__ == '__main__':
    unittest.main()
