"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""
import unittest

class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        pass

class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual("PAHNAPLSIIGYIR", self.sol.convert(s = "PAYPALISHIRING", numRows = 3))

    def test_sample01(self):
        self.assertEqual("PINALSIGYAHRPI", self.sol.convert(s = "PAYPALISHIRING", numRows = 4))

if __name__ == '__main__':
    if False:
        unittest.main()
    else:
        pass