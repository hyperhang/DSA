# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def print_linked_list(head: ListNode):
    while head!=None:
        print(head.val)
        head = head.next
        
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode :
        while head != None:
            if head.val == val:
                head = head.next
            else:
                break
        if head == None:
            return head
        start = head
        end = head.next
        if end == None:
            return start
        while end != None:
            if end.val != val:
                start = start.next
                end = end.next
            else:
                start.next = end.next
                end = end.next
        return head


s = Solution()
n1, n2, n3, n4, n5, n6, n7 = ListNode(1),ListNode(2), ListNode(6), ListNode(3),ListNode(4),ListNode(5), ListNode(6)
n1.next = n2
# n1.next = None

n2.next = n3
# n2.next = None

n3.next = n4
# n3.next = None
n4.next = n5
# n5.next = None
n5.next = n6
n6.next = n7

newHead = s.removeElements(n1, 5)
print_linked_list(newHead)