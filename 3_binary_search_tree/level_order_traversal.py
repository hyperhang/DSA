from collections import deque

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None
    
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        
        while len(q) != 0:
            next_level = deque()
            val = []
            while len(q) != 0:
                cur_node = q.popleft()
                val.append(cur_node.val)
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
            q = next_level
            ans.append(val)
        
        return ans
    
sol = Solution()

n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(sol.levelOrder(n1))
        
        
        