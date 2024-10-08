from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Solution 1
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        q = deque()
        q.append(root)
        
        while len(q) != 0:
            next_lvl = deque()
            prev = None
            while len(q) != 0:
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                
                if node.left:
                    next_lvl.append(node.left)
                    next_lvl.append(node.right)
            q = next_lvl
            
        return root
       
def print_lvl(node: Node):
    while node:
        first = node
        lvl = []
        while first :
            lvl.append(first.val)
            first = first.next
        print("lvl: ", lvl)
        node = node.left
         
         

# Solution 2
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        head = root
        while head:
            first = head
            while first:
                if first.left:
                    first.left.next = first.right
                else:
                    break
                
                if first.next:
                    first.right.next = first.next.left
                    first = first.next
                else:
                    break
            head = head.left
        return root
                
            
sol = Solution()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7

n = sol.connect(n1)
print_lvl(n)            

        