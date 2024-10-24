# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ar = []
        def in_order(node: TreeNode):
            if not node:
                return
            in_order(node.left)
            ar.append(node)
            in_order(node.right)
        
        in_order(root)
        min_greater = TreeNode(200)
        
        for node in ar[::]:
            if node.val > val and min_greater.val > node.val:
                min_greater = node
        ans = TreeNode(val)
        if min_greater.val == 200:
            ans.left = root
            return ans
        else:
            current_right = min_greater.right 
            if current_right:
                ans.left = current_right
            min_greater.right = ans
            return root
            
sol = Solution()

# n4 = TreeNode(4)
# n1 = TreeNode(1)
# n3 = TreeNode(3)
# n2 = TreeNode(2)
# n4.left = n1
# n4.right = n3
# n3.left = n2

# node = sol.insertIntoMaxTree(n4, 5)

# print(node.val)    
# print(node.left.val)    
# print(node.left.left.val, node.left.right.val)    
# print(node.left.right.left.val)    
  
            
n4 = TreeNode(4)
n1 = TreeNode(1)
n5 = TreeNode(5)
n2 = TreeNode(2)
n5.left = n2
n5.right = n4
n2.right = n1

node = sol.insertIntoMaxTree(n5, 3)

print(node.val)
print(node.left.val, node.right.val)    
print(node.left.right.val)    
print(node.right.right.val)  
            
        