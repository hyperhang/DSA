from typing import List
from collections import defaultdict

# class Solution:
#     def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
#         in_vertices = defaultdict(set)
#         out_vertices = defaultdict(set)
#         for n1, n2 in invocations:
#             in_vertices[n2].add(n1)
#             out_vertices[n1].add(n2)
        
#         suspicious = set([k])
        
#         def get_all_child(v):
#             for child in out_vertices[v]:
#                 if child in suspicious:
#                     continue
#                 suspicious.add(child)
#                 get_all_child(child)
                
#         get_all_child(k)
        
#         print("suspicious: ", suspicious)
#         suspicious_parents = set()
#         for v in suspicious:
#             print(f"in_vertices[{v}]: {in_vertices[v]}")
#             suspicious_parents = suspicious_parents.union(in_vertices[v])  
#             suspicious_parents.add(v)  
        
#         print("suspicious_parents: ", suspicious_parents)
#         full = [i for i in range(n)]
#         if suspicious_parents != suspicious:
#             return full
#         return list(set(full) - suspicious  )  






class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        in_vertices = defaultdict(set)
        out_vertices = defaultdict(set)
        for n1, n2 in invocations:
            in_vertices[n2].add(n1)
            out_vertices[n1].add(n2)
        suspicious = set()
        parents = set()
        
        def dfs(v):
            if child in suspicious:
                return
            suspicious.add(v)
            parents.add(v)
            for p in in_vertices[v]:
                parents.add(p)
            for child in out_vertices[v]:
                dfs(child)
                
        dfs(k)        
        full = [i for i in range(n)]
        if parents != suspicious:
            return full
        return list(set(full) - suspicious  )    
    
n = 4
k = 1
invocations = [[1,2],[0,1],[3,2]]  # [0,1,2,3]

n = 5
k = 0
invocations = [[1,2],[0,2],[0,1],[3,4]]  # [3,4]

n = 3
k = 2
invocations = [[1,2],[0,1],[2,0]]  # []

n = 2
k = 1
invocations = [[0,1]]


n = 2
k = 0
invocations = [[0,1]]  # []

n = 2
k = 0
invocations = []  # [1]

n = 3
k = 0
invocations = [[0,2],[2,1],[2,0]]  # []

sol = Solution()

print(sol.remainingMethods(n, k, invocations))

            