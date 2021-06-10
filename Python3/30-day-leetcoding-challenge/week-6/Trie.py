#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.


"""

import unittest
from typing import List, Set, Tuple, Dict

# import math

class Trie:
    value: str = None
    childs: Dict = None
    end: bool = False

    def __init__(self, value):
        """
        Initialize your data structure here.
        """
        self.value = value
        self.childs = {}

    def __str__(self):
        desc = f"\n{id(self):x} value: {self.value} childs: [{self.childs}] end={self.end}"
        result = desc
        for child in self.childs:
            result = result + f"{self.childs[child]}"
        return result


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word):
            char = word[0]
            word = word[1:]
            if not char in self.childs:
                temp = Trie(char)
                self.childs[char] = temp
            self.childs[char].insert(word)
        else:
            self.end = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        result = False

        if len(word):
            char = word[0]
            word = word[1:]
            if char in self.childs:
                result = self.childs[char].search(word)
        else:
            if self.end: result = True

        return result


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        result = False

        if len(prefix):
            char = prefix[0]
            prefix = prefix[1:]
            if char in self.childs:
                result = self.childs[char].startsWith(prefix)
        else:
            result = True

        return result



class TestMethods(unittest.TestCase):
    def trie_test(self, methods: List[str], args: List[List[str]]):
        print(f"\n\nmethods: {methods}\nargs:{args}")
        result = []
        trie = Trie("")
        for method, arg in zip(methods, args):
            try:
                func = getattr(trie, method)
                result.append(func(*arg))
            except AttributeError:
                pass

        print(f"trie:")
        print(trie)

        return result

    def test_sample00(self):
        self.assertEqual([],
                        self.trie_test(   ["Trie","insert","search","search","startsWith","insert","search"],
                                            [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
                                        )
                        )


if __name__ == '__main__':
    do_unittests = False

    if do_unittests:
        unittest.main()
    else:
        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
        test = TestMethods()
        # out = test.trie_test(   ["insert","search","search"],
        #                      [["apple"],["app"],["apple"]])
        # out = test.trie_test(   ["insert","startsWith","search","search"],
        #                      [["apple"],["app"],["apple"],["app"]])
        out = test.trie_test(   ["Trie","insert","search","search","startsWith","insert","search"],
                             [[],["apple"],["apple"],["app"],["app"],["app"],["app"]])
        print(out)



