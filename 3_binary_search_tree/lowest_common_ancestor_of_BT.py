# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         parent = dict()
        
#         def check(node: TreeNode):
#             if node:
#                 if node.left:
#                     parent[node.left] = node
#                 if node.right:
#                     parent[node.right] = node
#                 check(node.left)
#                 check(node.right)
#         check(root)
        
#         p1 = [p]
#         while p in parent:
#             p1.append(parent[p])
#             p = parent[p]
#         p2 = [q]
#         while q in parent:
#             p2.append(parent[q])
#             q = parent[q]
            
#         ans = None
#         i = 0
#         while i < min(len(p1), len(p2)) and p1[-1-i].val == p2[-1-i].val:
#             i += 1
#         ans = p1[-i].val
#         return ans
            


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(current_node: TreeNode) -> bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans






s = Solution()  
            
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

# res = s.lowestCommonAncestor(root, a5, a8)


n3 = TreeNode(3)
n5 = TreeNode(5)
n1 = TreeNode(1)

n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)

n7 = TreeNode(7)
n4 = TreeNode(4)

n3.left, n3.right = n5, n1
n5.left, n5.right = n6,n2
n1.left, n1.right = n0, n8
n2.left, n2.right = n7,n4

res = s.lowestCommonAncestor(n3, n5, n4)

print("res = ", res)