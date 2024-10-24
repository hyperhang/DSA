# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(max(nums))
        
        def seek(node: TreeNode, left, right):
            max_ele = max(nums[left:right+1])
            max_idx = nums.index(max_ele)
            node.val = max_ele
            if max_idx != left:
                node.left = TreeNode()
                seek(node.left, left, max_idx-1)
            if max_idx != right:
                node.right = TreeNode()
                seek(node.right, max_idx+1, right)
        
        seek(root, 0, len(nums)-1)
        
        return root
    
sol = Solution()
# nums = [3,2,1,6,0,5]
# node = sol.constructMaximumBinaryTree(nums)
# print(node.val, node.left.val, node.right.val)
# print(node.left.right.val, node.right.left.val)
# print(node.left.right.right.val)

nums = [3,2,1]
node = sol.constructMaximumBinaryTree(nums)
print(node.val, node.left.val,node.right.right.val)