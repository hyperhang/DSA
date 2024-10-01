# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def print_linked_list(head: ListNode):
    while head!=None:
        print(head.val, end = ", ")
        head = head.next
    print()
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        first = head
        if first == None:
            return None
        second = head.next
        if second == None:
            return first
        start_1 = first
        start_2 = second
        while second != None and second.next != None:
            a = second.next
            b = a.next
            first.next = a
            second.next = b
            first = a
            second = b
        first.next = start_2
        
        print_linked_list(start_1)
        return start_1
        


s = Solution()
# n1, n2, n3, n4, n5 = ListNode(1),ListNode(2), ListNode(3),ListNode(4),ListNode(5)
n1, n2, = ListNode(1),ListNode(2), 
n1.next = None
# n1.next = n2
# n1.next = None

# n2.next = n3
n2.next = None

# n3.next = n4
# n3.next = None
# n4.next = n5
# n5.next = None
# n5.next = n6
# n6.next = n7

newHead = s.oddEvenList(n1)
print_linked_list(newHead)