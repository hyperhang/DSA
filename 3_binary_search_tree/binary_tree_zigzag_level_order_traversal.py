# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque()
        q.append(root)
        ans = []
        flag = True
        
        while len(q) != 0:
            next_lvl = deque()
            cur_val = []
            while len(q) != 0:
                node = q.popleft()
                cur_val.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            print("lvl: ", cur_val)
            if flag:
                ans.append(cur_val)
            else:
                ans.append(cur_val[::-1])
            q = next_lvl
            flag = not flag
        return ans
    
sol = Solution()

n1 = TreeNode(3)        
n2 = TreeNode(9)        
n3 = TreeNode(20)        
n4 = TreeNode(15)        
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left =  n4
n3.right = n5     
            
print(sol.zigzagLevelOrder(n1))