# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        def spread(node: TreeNode, start: int, end: int):
            print("---"*10)
            print(f"start: {start}, end: {end}")
            if start == end:
                node.val = nums[start]
                return
            if start + 1 == end:
                print("node.val: ", node.val)
                node.val = nums[end]
                print("node.val: ", node.val)
                node.left = TreeNode(nums[start])
                print("node.left.val: ", node.left.val)
                return
            
            mid = (end - start)//2 + start
            node.val = nums[mid]
            
            node.left = TreeNode()
            node.right = TreeNode()
            spread(node.left, start, mid-1)
            spread(node.right, mid+1, end)
        
        spread(root, 0, len(nums)-1)
        return root
    
sol = Solution()

# nums = [-10,-3,0,5,9]
# root = sol.sortedArrayToBST(nums)
# print(root.val)
# print(root.left.val, root.right.val)
# print(root.left.left.val, root.right.left.val)


nums = [1,3]
root = sol.sortedArrayToBST(nums)
print(root.val)
print(root.left.val)

        