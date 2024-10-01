from typing import List

# 15.52
class QuickUnion:
    root = None
    rank = None
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_y] < self.rank[root_x]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_x] += 1
        

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        qu = QuickUnion(n)
        for e1, e2 in edges:
            qu.union(e1, e2)
        return qu.find(source) == qu.find(destination)
    
s = Solution()
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

print(s.validPath(n, edges, source, destination))            
