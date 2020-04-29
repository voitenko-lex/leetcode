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
        lstResult = []
        strResult = ""
        substr = s

        while True:
            if len(substr)>numRows:
                lstResult.append(list(substr[:numRows]))
                substr = substr[numRows:]
            elif len(substr)>0:
                lstResult.append(list(substr))
                substr = ""
            else:
                break

            if len(substr)>(numRows-2):
                if numRows>1:
                    lstResult.append([str('')] + list(substr[:(numRows-2)][::-1]))
                else:
                    lstResult.append(list(substr[:(numRows-2)][::-1]))          
                substr = substr[(numRows-2):]
            elif len(substr)>0:
                if numRows>1:
                    lstResult.append([str('')] + list(substr[::-1]))
                else:
                    lstResult.append(list(substr[::-1]))

                substr = ""
            else:
                break

        for i in range(numRows):
            for j in range(len(lstResult)):
                try:
                    # print(f"j = {j}, i = {i} {str(lstResult[j][i])}")
                    strResult += str(lstResult[j][i])
                except IndexError:
                    pass


        print(f"lstResult = {lstResult} len:{len(lstResult)}")
        print(f"strResult = {strResult}")

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

if __name__ == '__main__':
    if False:
        unittest.main()
    else:
        sol = Solution()
        sol.convert(s = "ABCD", numRows = 1)
        # sol.convert(s = "123456789", numRows = 3)
