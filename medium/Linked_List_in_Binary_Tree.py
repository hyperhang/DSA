# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    included = False
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def check_path(node_tree: Optional[TreeNode], node_list: Optional[ListNode]):
            if self.included  :
                return
            if node_list == None :
                self.included = True
                return 
            if  node_tree == None:
                return
            if node_tree.val == node_list.val:
                check_path(node_tree.left, node_list.next)
                check_path(node_tree.right, node_list.next)
            
        def check(node_tree: Optional[TreeNode]):
            if self.included or node_tree == None:
                return
            check_path(node_tree, head)
            check(node_tree.left)
            check(node_tree.right)
        
        check(root)
        return self.included
    
s = Solution()

n1 = TreeNode(1)

n4_21 = TreeNode(4)
n4_22 = TreeNode(4)

n2_31 = TreeNode(2)
n2_32 = TreeNode(2)

n1_4 = TreeNode(1)       
n6_4 = TreeNode(6)       
n8_4 = TreeNode(8)   
    
n1_5 = TreeNode(1)       
n3_5 = TreeNode(3)     
  
n1.left = n4_21
n1.right = n4_22
n4_21.right = n2_31
n4_22.left = n2_32
n2_31.left = n1_4
n2_32.left = n6_4
n2_32.right = n8_4
n8_4.left = n1_5
n8_4.right = n3_5             
                
l4 = ListNode(4)          
l2 = ListNode(2)          
l8 = ListNode(8)    
l4.next = l2
l2.next = l8  # True
          
# l4 = ListNode(4)          
# l2 = ListNode(2)          
# l8 = ListNode(8)    
# l4_1 = ListNode(4)      
# l4.next = l2
# l2.next = l8
# l8.next = l4_1 # False

# l4 = ListNode(4)          
# l2 = ListNode(2)          
# l9 = ListNode(9)    
# l4.next = l2
# l2.next = l9   # False


# l1 = ListNode(1)
# l4 = ListNode(4)          
# l2 = ListNode(2)          
# l6 = ListNode(6)  
# l8 = ListNode(8)  
# l1.next = l4  
# l4.next = l2
# l2.next = l6 
# l6.next = l8 # False

# print(s.isSubPath(l1, n1))

print(s.isSubPath(l4, n1))