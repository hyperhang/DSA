# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            first = head
            while first and not (first.left or first.right):
                first = first.next
            head = first
            if head:
                head = head.left if head.left else head.right
                while first:
                    second = first.next
                    while second and not (second.left or second.right):
                            second = second.next
                    tem = None
                    if second:        
                        tem = second.left if second.left else second.right
                        
                    if first.left:
                        if first.right:
                            first.left.next = first.right
                            first.right.next = tem
                        else:
                            first.left.next = tem
                    else:
                        first.right.next = tem
                    first = second
        return root




class Solution:
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        if not root:
            return root
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
        return root
    


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        leftmost = root
        while leftmost:
            curr = leftmost
            leftmost = None
            prev = None
            while curr:
                for child in (curr.left, curr.right):
                    if child:
                        if prev:
                            prev.next = child
                        else:
                            leftmost = child
                        prev = child

                curr = curr.next

        return root

def print_lvl(node: Node):
    while node:
        first = node
        lvl = []
        while first :
            lvl.append(first.val)
            first = first.next
        print("lvl: ", lvl)
        while node and not (node.left or node.right):
            node = node.next
        if node:
            node = node.left if node.left else node.right
         
         
   
sol = Solution()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
# n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left, n2.right = n4, n5
n3.right = n7

n = sol.connect(n1)
print_lvl(n)        
        