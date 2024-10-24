from typing import List

class TreeNode:
    def __init__(self, val=0) -> None:
        self.val = val
        self.left = None
        self.right = None
    
# def insert(root: TreeNode, val:int):
#     while root.val != 0:
#         if root.val > val:
#             if not root.left :
#                 root.left = TreeNode()
#             root = root.left
#         else:
#             if not root.right:
#                 root.right = TreeNode()
#             root = root.right
#     root.val = val
    
#     # if root.val > val:
#     #     if not root.left:
#     #         root.left = TreeNode(val)
#     #     else:
#     #         insert(root.left, val)
#     # else:
#     #     if not root.right:
#     #         root.right = TreeNode(val)
#     #     else:
#     #         insert(root.right, val)
            
        
    
        
# class Solution:
#     def verifyPreorder(self, preorder: List[int]) -> bool:
#         real_pre = []
        
#         def dfs(node : TreeNode) :
#             if node:
#                 real_pre.append(node.val)
#                 dfs(node.left)
#                 dfs(node.right)
                
#         root = TreeNode(preorder[0])
#         for ele in preorder[1:]:
#             insert(root, ele)
        
#         dfs(root)
#         if real_pre == preorder:
#             return True
#         return False
#     # TLE, O(N^2)





class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -1e9
        stack = []
        for num in preorder:
            while stack and stack[-1] < num:
                min_limit = stack.pop()
            if num <= min_limit:
                return False
            stack.append(num)        
        return True


s = Solution()
preorder = [5,2,1,3,6]
preorder = [5,2,6,1,3]
print(s.verifyPreorder(preorder))
            
  
        