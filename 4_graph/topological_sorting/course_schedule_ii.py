from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_vertices = defaultdict(set)
        out_vertices = defaultdict(set)
        for second, first in prerequisites:
            in_vertices[second].add(first)
            out_vertices[first].add(second)
            
        o_in = set([i for i in range(numCourses)]) - set(in_vertices.keys())
        ans = []
        while len(o_in) != 0:
            children_o_in = set()
            while len(o_in) != 0:
                ele = o_in.pop()
                ans.append(ele)
                for child in out_vertices[ele]:
                    in_vertices[child].discard(ele)
                    if len(in_vertices[child]) == 0:
                        children_o_in.add(child)
            o_in = children_o_in
        
        if len(ans ) != numCourses:
            return []
        return ans

sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

numCourses = 2
prerequisites = [[1,0]]

numCourses = 1
prerequisites = []
sol.findOrder(numCourses, prerequisites)           
            