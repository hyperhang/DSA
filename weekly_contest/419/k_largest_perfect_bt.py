# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        dp = dict()
        all = []
        def check(node: TreeNode):
            if (not node.left) and (not node.right):
                dp[node] = 1
                all.append(1)
                return 
            if node.left and node.left not in dp:
                check(node.left)
            if node.right and node.right not in dp:
                check(node.right)
            if node.left and node.right and dp[node.left] == dp[node.right] and dp[node.left] != 0:
                dp[node] = dp[node.right]*2 + 1
                all.append(dp[node])
                return
            dp[node] = 0
            return
        
        check(root)
        all = sorted(all, reverse=True)
        return all[k-1] if k > len(all) else -1
    
sol = Solution()

# n5 = TreeNode(5)
# n3 = TreeNode(3)
# n6 = TreeNode(6)
# n5_3_1 = TreeNode(5)
# n2_3 = TreeNode(2)
# n5_3_2 = TreeNode(5)
# n7_3 = TreeNode(7)
# n1 = TreeNode(1)
# n8_4_1 = TreeNode(8)
# n6_4 = TreeNode(6)
# n8_4_2 = TreeNode(8)

# n5.left, n5.right = n3, n6
# n3.left,n3.right = n5_3_1, n2_3
# n6.left, n6.right = n5_3_2, n7_3
# n5_3_1.left, n5_3_1.right = n1, n8_4_1
# n5_3_2.left, n5_3_2.right = n6_4, n8_4_2


# n7 = TreeNode(7)
# n4 = TreeNode(4)
# n7.left = n4

n10 = TreeNode(10)
n6 = TreeNode(6)
n2 = TreeNode(2)
n11 = TreeNode(11)
n10_3 = TreeNode(10)
n10.left, n10.right = n6, n2
n6.right = n11
n2.left = n10_3

print(sol.kthLargestPerfectSubtree(n10, 1))
