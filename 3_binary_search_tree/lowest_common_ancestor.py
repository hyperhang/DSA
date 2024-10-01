# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        start = root
        a = min(p.val, q.val)
        b = max(p.val, q.val)
        print("a: ", a, "  ---   b: ", b)
        while True:
            val = start.val
            print("val ", val)
            if (val < b and val > a) or val == a or val == b :
                return start
            if val < a :
                start = start.right
                continue
            if val > b:
                start = start.left
                continue
            
root = TreeNode(6)
a2 = TreeNode(2)
a8 = TreeNode(8)
a0 = TreeNode(0)
a4 = TreeNode(4)
a7 = TreeNode(7)
a9 = TreeNode(9)
a3 = TreeNode(3)
a5 = TreeNode(5)

root.left = a2
root.right = a8

a2.left = a0
a2.right = a4

a4.left = a3
a4.right = a5

a8.left = a7
a8.right = a9

s = Solution()
res = s.lowestCommonAncestor(root, a2, a8)
print("res = ", res)