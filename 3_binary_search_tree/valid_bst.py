# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     bst = []
#     def isValidBST(self, root: TreeNode) -> bool:

#         def check_node(node: TreeNode):
#             if not node:
#                 return
#             if node.left:
#                 check_node(node.left)
#             self.bst.append(node.val)
#             check_node(node.right)
            
        
#         check_node(root)
#         print("bst: ", self.bst)
#         for i in range(1,len(self.bst)):
#             if self.bst[i] <= self.bst[i-1]:
#                 self.bst = []
#                 return False
#         self.bst = []
#         return True
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.bst = []  # Initialize bst list inside the function

        def check_node(node: TreeNode):
            if not node:
                return
            if node.left:
                check_node(node.left)
            self.bst.append(node.val)  # Append the current node's value
            if node.right:
                check_node(node.right)

        check_node(root)
        print("bst: ", self.bst)
        for i in range(1, len(self.bst)):
            if self.bst[i] <= self.bst[i - 1]:
                return False
        return True
    
s = Solution()

n5 = TreeNode(5)
n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(7)
n0 = TreeNode(0)

n5.left = n4
n5.right = n6
n6.left = n3
n6.right = n7   

print(s.isValidBST(n0))