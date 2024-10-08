class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    last_element = -1e9
    flag = True
    def is_bst(self, root: Node):
        
        def dfs(node: Node):
            if not node:
                return
            dfs(node.left)
            if node.val <= self.last_element:
                self.flag = False
                return
            else:
                self.last_element = node.val
            dfs(node.right)
        
        dfs(root)
        
        return self.flag

sol = Solution()

n1 = Node(5)   
n2 = Node(1)   
n3 = Node(4)   
n4 = Node(3)   
n5 = Node(6)   

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

# n1 = Node(2)
# n1.left = Node(1)
# n1.right = Node(3)

# n1 = Node(5)
# n2 = Node(4)
# n3 = Node(6)
# n4 = Node(3)
# n5 = Node(7)
# n1.left = n2
# n1.right = n3
# n3.left = n4
# n3.right = n5

n1 = Node(0)
print(sol.is_bst(n1))  
  
    