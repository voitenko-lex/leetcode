#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
### Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5

   Hide Hint #1  
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
   Hide Hint #2  
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
   Hide Hint #3  
Topological sort could also be done via BFS.

"""

import unittest
from typing import List, Set, Tuple, Dict
import collections

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = {}
#         for k, it in groupby(sorted(prerequisites), key=lambda x: x[0]):
#             graph[k] = {e for _, e in it}
        
#         # отрубаем все вершины которые не могут быть частью цикла (имеющие только входящие или только выходящие ребра)
#         sub_graph = {}
#         while True:
#             vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
#             sub_graph = {k: vertex_set & vs for k, vs in graph.items()
#                          if k in vertex_set and vertex_set & vs}
#            # print(sub_graph)
#             #print(graph)

#             if sub_graph == graph:
#                 break
#             else:
#                 graph = sub_graph
#         if graph:
#             return False
#         else:
#             return True

class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     print(f"canFinish({numCourses}, {prerequisites})")
    #     connections = collections.defaultdict(dict)
    #     counters = collections.defaultdict(dict)
    #     free_nodes = []
        
    #     for a, b in prerequisites:
    #         connections[a][b] = 1
    #         connections[b][a] = 1
        
    #     for connection in connections:
    #         counters[len(connections[connection])][connection] = 1
        
    #     print(f"connections = {connections}")
    #     print(f"counters = {counters}")

    #     while len(counters[1])>0:
    #         single, _ = counters[1].popitem()
    #         linked_node = connections.pop(single)
    #         if linked_node:
    #             linked_node = list(linked_node)[0]
    #             linked_node_weight = len(connections[linked_node])
    #             connections[linked_node].pop(single)
    #             if linked_node_weight > 1:
    #                 weight = counters[linked_node_weight].pop(linked_node)
    #                 counters[linked_node_weight - 1][linked_node] = weight
    #         free_nodes.append(single)

    #     print("=" * 20)
    #     print(f"connections = {connections}")
    #     print(f"counters = {counters}")
    #     print(f"free_nodes = {free_nodes}")

    #     if numCourses <= len(free_nodes):
    #         return True
    #     else:
    #         return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print(f"canFinish({numCourses}, {prerequisites})")
        connections = collections.defaultdict(dict)
        counters = collections.defaultdict(dict)
        free_nodes = []
        
        for a, b in prerequisites:
            connections[a][b] = 1
        
        for connection in connections:
            counters[len(connections[connection])][connection] = 1
        
        print(f"connections = {connections}")
        print(f"counters = {counters}")

        # while len(counters[0])>0:
        #     single, _ = counters[1].popitem()
        #     linked_node = connections.pop(single)
        #     if linked_node:
        #         linked_node = list(linked_node)[0]
        #         linked_node_weight = len(connections[linked_node])
        #         connections[linked_node].pop(single)
        #         if linked_node_weight > 1:
        #             weight = counters[linked_node_weight].pop(linked_node)
        #             counters[linked_node_weight - 1][linked_node] = weight
        #     free_nodes.append(single)

        # print("=" * 20)
        # print(f"connections = {connections}")
        # print(f"counters = {counters}")
        # print(f"free_nodes = {free_nodes}")

        if numCourses <= len(free_nodes):
            return True
        else:
            return False


class TestMethods(unittest.TestCase):
    sol = Solution()

    def test_sample00(self):
        test_input = self.sol.canFinish(numCourses = 2, prerequisites = [[1,0]])
        test_output = True
        self.assertEqual(test_output, test_input)

    def test_sample01(self):
        test_input = self.sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])
        test_output = False
        self.assertEqual(test_output, test_input)


if __name__ == '__main__':
    if False:
        unittest.main()
    else:
        sol = Solution()
        print(sol.canFinish(numCourses = 2, prerequisites = [[0,1],[1,2]]))



