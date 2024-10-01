from typing import List

class QuickUnion:
    root = []
    rank = []
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x) -> int:
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
           
    def is_connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)
            
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = []
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j]:
                    edges.append([i, j])
        print("init edges: ", edges)
        qu = QuickUnion(len(isConnected))
        for e in edges:
            qu.union(e[0], e[1])
        roots = set()
        for i in range(len(isConnected)):
            r = qu.find(i)
            roots.add(r)
        print("# roots : ", len(roots))
        return len(roots)
    
s = Solution()
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
s.findCircleNum(isConnected)