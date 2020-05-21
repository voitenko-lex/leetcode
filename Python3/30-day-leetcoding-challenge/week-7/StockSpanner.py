#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
## Online Stock Span

Write a class StockSpanner which collects daily price quotes for some stock, 
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of 
consecutive days (starting from today and going backwards) for which the 
price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], 
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

 

Note:

    Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
    There will be at most 10000 calls to StockSpanner.next per test case.
    There will be at most 150000 calls to StockSpanner.next across all test cases.
    The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

"""

import unittest
# import logging
from typing import List, Set, Tuple, Dict
# import collections

class Stock:
    def __init__(self, price):
        self.price = price
        self.previous = None
        self.stockspan_value = 0
        self.stockspan_last = None

    def __str__(self):
        desc = f"\n{id(self)} price: {self.price} \
            previous: {id(self.previous) if self.previous else None} \
            stockspan_value = {self.stockspan_value}, \
            stockspan_last = {id(self.stockspan_last) if self.stockspan_last else None}"

        if self.previous: desc = desc + f"{self.previous}"
        return desc
    
    def get_stockspan(self, level):
        stockspan_value = 0
        stockspan_last = self
        if self.price <= level:
            stockspan_value += 1
            stockspan_last = self.previous
            if self.previous: 
                prev_stockspan_value, prev_stockspan_last = self.previous.get_stockspan(level)
                stockspan_value += prev_stockspan_value
                if prev_stockspan_last: stockspan_last = prev_stockspan_last
        
        return stockspan_value, stockspan_last

    def get_stockspan_fast(self, level):
        if level == 85:
            print("")

        stockspan_value = 0
        stockspan_last = None
        if self.price <= level:
            stockspan_value += 1

            if self.stockspan_value > 1:
                stockspan_last = self.stockspan_last
                stockspan_value = self.stockspan_value
            elif self.previous: 
                stockspan_last = self.previous
            
            if stockspan_last:
                prev_stockspan_value, prev_stockspan_last = stockspan_last.get_stockspan_fast(level)
                stockspan_value += prev_stockspan_value
                stockspan_last = prev_stockspan_last
        else:
            stockspan_last = self

        return stockspan_value, stockspan_last

class StockSpanner:

    def __init__(self):
        self.last = None
        
    def next(self, price: int) -> int:
        next_stock = Stock(price)
        next_stock.previous = self.last
        self.last = next_stock

        # stockspan_value, stockspan_last = self.last.get_stockspan(self.last.price)
        stockspan_value, stockspan_last = self.last.get_stockspan_fast(self.last.price)
        self.last.stockspan_value = stockspan_value
        self.last.stockspan_last = stockspan_last

        return stockspan_value
    
    def __str__(self):
        return f"{self.last}"
    

        


class TestMethods(unittest.TestCase):
    def stockspanner_test(self, methods: List[str], args: List[List[str]]):
        print(f"\n\nmethods: {methods}\nargs:{args}")
        result = []
        stockspanner = StockSpanner()
        for method, arg in zip(methods, args):
            # func = getattr(stockspanner, method)
            # stock_span = func(*arg)
            # print(f"method = {method} arg = {arg} stock_span = {stock_span} ")
            # result.append(stock_span)            
            
            try:
                func = getattr(stockspanner, method)
                stock_span = func(*arg)
                # print(f"method = {method} arg = {arg} stock_span = {stock_span} ")
                result.append(stock_span)
            except AttributeError:
                pass


        
            print("="*20)
            print(stockspanner)

        return result
    
    def test_sample00(self):
        self.assertEqual([1, 1, 1, 2, 1, 4, 6], 
                        self.stockspanner_test( ["StockSpanner","next","next","next","next","next","next","next"],
                                                [[],[100],[80],[60],[70],[60],[75],[85]])
                        )
        
    def test_sample01(self):
        self.assertEqual([1,2,3,4,5], 
                        self.stockspanner_test( ["StockSpanner","next","next","next","next","next"],
                                                [[],[31],[41],[48],[59],[79]])
                        )

       

    
if __name__ == '__main__':
    if True:
        unittest.main()
    else:
        # Your StockSpanner object will be instantiated and called as such:
        # obj = StockSpanner()
        # param_1 = obj.next(price)

        test = TestMethods()
        out = test.stockspanner_test(   ["StockSpanner","next","next","next","next","next","next","next"],
                                        [[],[100],[80],[60],[70],[60],[75],[85]])
        # out = test.stockspanner_test(   ["StockSpanner","next","next","next","next","next"],
        #                                 [[],[10],[20],[30],[40],[50]])
        print(out)


