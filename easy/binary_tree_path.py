# Definition for a binary tree node.
import copy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    path = []
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        def check(parent, path_i):
            if parent == None:
                # self.path.append(path_i)
                # print("path_i: ", self.path)
                return
            path_i.append(parent.val)
            if parent.left == None and parent.right == None:
                self.path.append(path_i)
                return
            check(parent.left, copy.deepcopy(path_i) )
            check(parent.right, copy.deepcopy(path_i) )
        check(root, [])
        self.path = [ '->'.join(map(str, element)) for element in self.path]
        print(self.path)
        self.path = []
        return self.path
        
s = Solution()
"""
        1
     2     3
  4    5
6     7
"""
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n4.left = n6
# n5.left = n7
ar = {}
ar[n1] = 10
ar[n2] = 11
ar[n3] = 12
print(ar[n2])
# s.binaryTreePaths(n1)