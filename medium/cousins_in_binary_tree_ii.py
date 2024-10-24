# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = [root]
        root.val = 0
        while current:
            children = []
            all_sum = 0 # sum of all chidren
            for node in current:
                all_sum += node.left.val if node.left else 0
                all_sum += node.right.val if node.right else 0
            for node in current:   # update all children values                
                left = node.left.val if node.left else 0
                right = node.right.val if node.right else 0
                if node.left:
                    node.left.val = all_sum - left - right
                    children.append(node.left)
                if node.right:
                    node.right.val = all_sum - left - right
                    children.append(node.right)
            current = children
        return root
        # TC: O(N)
        # SC: O(N)
    

n5 = TreeNode(5)
n4 = TreeNode(4)
n9 = TreeNode(9)
n1 = TreeNode(1)
n10 = TreeNode(10)
n2 = TreeNode(2)
n7 = TreeNode(7)
n5.left, n5.right = n4, n9
n4.left, n4.right = n1, n10
n9.left, n9.right = n2, n7


sol = Solution()
new_root = sol.replaceValueInTree(n5)
print(new_root.val)
print(new_root.left.val, new_root.right.val)
print(new_root.left.left.val, new_root.left.right.val, new_root.right.left.val, new_root.right.right.val)

            
                