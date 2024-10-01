# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printll(self, node):
        head = node
        res = [node.val]
        node = node.next
        while node != head:
            res.append(node.val)
            node = node.next
        print(res)
            
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        length = 1
        iter = list
        iter = iter.next 
        while iter != list:
            length += 1
            iter = iter.next
        len_first = (length + 1) // 2
        len_second = length - len_first
        print("1st len = ", len_first)
        print("2nd len = ", len_second)
        
        iter = list
        before_iter = None
        first_node = iter
        second_node = None
        while len_first != 0:
            len_first -= 1
            before_iter = iter
            iter = iter.next
        before_iter.next = first_node
        
        second_node = iter
        while iter != first_node:
            before_iter = iter
            iter = iter.next
        before_iter.next = second_node
        self.printll(first_node)
        self.printll(second_node)
        return [first_node, second_node]
            
s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

# n1.next = n5
# n5.next = n7
# n7.next = n1

n2.next = n6
n6.next = n1
n1.next = n5
n5.next = n2

s.splitCircularLinkedList(n2)