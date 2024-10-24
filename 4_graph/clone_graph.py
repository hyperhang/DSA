
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

#         visited = {}
        
#         def dfs(node: Node) -> Node:
#             if node in visited:
#                 return visited[node]
            
#             clone = Node(node.val)
#             visited[node] = clone
            
#             for neighbor in node.neighbors:
#                 clone.neighbors.append(dfs(neighbor))
            
#             return clone
        
#         return dfs(node)
#         # TC: O(V+E) 
#         # SC: O(V)
    

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        stack = [node]
        dup = Node(node.val)
        while stack:
            for ele in stack:
                
            

    
    
sol = Solution()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

dup = sol.cloneGraph(n1)
print(dup.val)
for nei in dup.neighbors:
    print(nei.val)
    print([ele.val for ele in nei.neighbors])
    