#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of integers and an integer k, you need to find the total number of continuous 
subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
"""

import unittest
from typing import List, Set, Tuple, Dict

class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     result = 0

    #     for i in range(len(nums)):
    #         print(f"init i = {i}")
    #         sum = nums[i]
    #         while True:
    #             if sum == k:
    #                 result += 1
    #             if (i < (len(nums)-1)):
    #                 i += 1
    #                 sum += nums[i]
    #             else:
    #                 break
    #     return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sums = []
        sums_hash = {}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            sums.append(sum)
            if sum in sums_hash:
                sums_hash[sum].append(i)
            else:
                sums_hash[sum] = [i]

        # print(f"k = {k}")
        # print(f"sums = {sums}")
        # print(f"sums_hash = {sums_hash}")
        
        for i in range(len(sums)):
            if sums[i] == k: result += 1
            diff = k + sums[i]
            # print(f"i = {i} sums[i]={sums[i]} diff = {diff}")
            if diff in sums_hash:
                for j in sums_hash[diff]:
                    if j > i:
                        result += 1
                        # print(f"{sums[j]}({j}) - {sums[i]}({i})")

        return result
            
            


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual(2, self.sol.subarraySum([1,1,1], k=2))

    def test_sample01(self):
        self.assertEqual(0, self.sol.subarraySum([], k=5))

    def test_sample02(self):
        self.assertEqual(1, self.sol.subarraySum([1], k=1))

    def test_sample03(self):
        self.assertEqual(2, self.sol.subarraySum([100,1,2,3,4], k=3))

    def test_sample04(self):
        self.assertEqual(1, self.sol.subarraySum([28,54,7,-70,22,65,-6], k=100))

    def test_sample05(self):
        self.assertEqual(55, self.sol.subarraySum([0,0,0,0,0,0,0,0,0,0], k=0))

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        # print(sol.subarraySum([1, 1, 3, -4, 0, 4], k=4))
        # print(sol.subarraySum([1]*10, k=10))
        print(sol.subarraySum(range(-5,20000), k=10))
        # print(sol.subarraySum([100,1,2,3,4], k=3))