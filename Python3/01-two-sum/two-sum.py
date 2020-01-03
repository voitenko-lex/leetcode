#!/usr/bin/env python
# -*- coding: utf-8 -*-
        
import unittest

class Solution:
#   First Solution  
    # def twoSum(self, nums, target):
    #     tnums = tuple(nums)
    #     for first_el, first_el_val in enumerate(tnums):
    #         for second_el, second_el_val in enumerate(tnums[first_el+1:]):
    #             if first_el_val + second_el_val == target:
    #                 return [first_el, first_el + 1 + second_el]
    
#   Second Solution 
    # def twoSum(self, nums, target):
    #     dnums = {y:x for x,y in enumerate(nums)}
    #     print(nums)
    #     print(dnums)
    #     for first_el, first_el_val in enumerate(nums):
    #         complement = dnums.get(target - first_el_val)
    #         if complement != None and complement != first_el:
    #             return [first_el, complement]
        
    #     raise AttributeError("No two sum solution")


#   Third Solution 
    def twoSum(self, nums, target):
        dnums = {}
        print(nums)
        for first_el, first_el_val in enumerate(nums):
            print(dnums)
            complement = dnums.get(target - first_el_val)
            if complement != None and complement != first_el:
                return [complement, first_el]
            else:
                dnums[first_el_val]=first_el
        
        raise AttributeError("No two sum solution")


class TestStringMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input_nums = [2, 7, 11, 15]
        test_input_target = 9
        test_output = [0, 1]
        self.assertEqual(self.sol.twoSum(test_input_nums, test_input_target), test_output)

    def test_sample01(self):
        test_input_nums = [3,2,4]
        test_input_target = 6
        test_output = [1, 2]
        self.assertEqual(self.sol.twoSum(test_input_nums, test_input_target), test_output)

if __name__ == '__main__':
    unittest.main()
