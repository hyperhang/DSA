# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        result = []
        def check_tree(node):
            if node.left :
                check_tree(node.left)
            if node.right:
                check_tree(node.right)
            result.append(node.val)
        if root:
            check_tree(root)
        print(result)
        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
#     1
# 2        3
#        4

# n1.left = n2
# n1.right = n3
# n3.left = n4

s = Solution()
s.postorderTraversal(None)