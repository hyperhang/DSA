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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None
        if head.next.next == None:
            if n == 1:
                head.next = None
            else:
                head = head.next
            return head
        # length >= 3
        pre_start = head
        start = head.next
        end = head.next
        while n > 1:
            if end.next != None:
                end = end.next
                n -= 1
            else:
                head = head.next
                return head
        while end.next != None:
            pre_start = pre_start.next
            start = start.next
            end = end.next
        pre_start.next = start.next
        return head

s = Solution()
n1, n2, n3, n4, n5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
n1.next = n2
# n1.next = None

n2.next = n3
# n2.next = None

# n3.next = n4
n3.next = None
n4.next = n5
n5.next = None

newHead = s.removeNthFromEnd(n1, 3)
print_linked_list(newHead)