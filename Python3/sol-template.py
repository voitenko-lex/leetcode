#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Description

"""

import unittest
from typing import List, Set, Tuple, Dict
# import collections

class Solution:
    def foo(self, num: int) -> List[int]:
        result = 0
        return result


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.foo(2)
        test_output = [0,1]
        self.assertEqual(test_output, test_input)


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        sol = Solution()
        print(sol.foo(20))



