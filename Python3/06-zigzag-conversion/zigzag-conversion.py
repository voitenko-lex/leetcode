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
    def convert(self, s: str, numRows: int) -> str:
        lstResult = [[str("")] * numRows]
        strResult = ""
        
        state = "zig"
        col = 0
        row = 0

        for char in s:

            while True:
                # print(f"char = {char} row = {row} col = {col}")
                if row < 0:
                    row = 0
                elif row == 0:
                    state = "zig"
                    break
                elif row >= numRows:
                    row = numRows - 2
                    lstResult.append([str("")] * numRows)
                    col += 1
                    state = "zag"
                else:
                    break
            
            lstResult[col][row] = char

            if state == "zig":
                row += 1
            else:
                lstResult.append([str("")] * numRows)
                col += 1
                row -= 1


        # print(f"lstResult = {lstResult}")
        
        for row in range(numRows):
            for col in range(len(lstResult)):
                strResult += lstResult[col][row]
        
        # print(f"strResult = {strResult}")
        return strResult


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        self.assertEqual("PAHNAPLSIIGYIR", self.sol.convert(s = "PAYPALISHIRING", numRows = 3))

    def test_sample01(self):
        self.assertEqual("PINALSIGYAHRPI", self.sol.convert(s = "PAYPALISHIRING", numRows = 4))

    def test_sample02(self):
        self.assertEqual("ABC", self.sol.convert(s = "ABC", numRows = 1))

    def test_sample03(self):
        self.assertEqual("ABCD", self.sol.convert(s = "ABCD", numRows = 1))

    def test_sample04(self):
        self.assertEqual("ACEBDF", self.sol.convert(s = "ABCDEF", numRows = 2))

if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        sol = Solution()
        # sol.convert(s = "ABC", numRows = 1)
        # sol.convert(s = "ABCDEF", numRows = 2)
        sol.convert(s = "123456789", numRows = 1)
