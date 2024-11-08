# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def check(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if (not node1) and (not node2): # both are None
                return True
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                if check(node1.left, node2.left) and check(node1.right, node2.right):
                    return True
                if check(node1.left, node2.right) and check(node1.right, node2.left):
                    return True
                return False
                    
            return False
        
        return check(root1, root2)
        
        