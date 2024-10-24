# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        children = [root]
        while children:
            next_children = []
            cur_sum = 0
            for node in children:
                cur_sum += node.val
                if node.left:
                    next_children.append(node.left)
                if node.right:
                    next_children.append(node.right)
            sums.append(cur_sum)
            children = next_children
        
        sums.sort(reverse=True)
        if k > len(sums):
            return -1
        return sums[k-1]
    
# n5 = TreeNode(5)
# n8 = TreeNode(8)
# n9 = TreeNode(9)
# n2 = TreeNode(2)
# n1 = TreeNode(1)
# n3 = TreeNode(3)
# n7 = TreeNode(7)
# n4 = TreeNode(4)
# n6 = TreeNode(6)
# n5.left, n5.right = n8, n9      
# n8.left, n8.right = n2, n1
# n9.left, n9.right = n3, n7
# n2.left, n2.right = n4, n6

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n2.left = n3

sol = Solution()
k = 3
print(sol.kthLargestLevelSum(n1, k))          
                