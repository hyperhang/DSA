from typing import List
from collections import defaultdict
import copy

class Solution:
    res = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        child = dict()
        n = len(graph)
        for i, v in enumerate(graph):
            child[i] = v
        # print("Child:\n", child)
        
        def check(node: int, path: list):
            path.append(node)
            # print("node: ", node)
            if node == n-1:
                self.res.append(path)
                return
            if node not in child: # leaf
                return
            for c in child[node]:
                # print("child: ", c)
                _path = copy.deepcopy(path)
                check(c, _path)
                
        check(0, [])
        return self.res
    
    
s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
graph = [[1,2],[3],[3],[]]
print(s.allPathsSourceTarget(graph))                
            