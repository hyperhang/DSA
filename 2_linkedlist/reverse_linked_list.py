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
    result = None
    def back(self, node0, node1, node2):   
        node1.next = node0     
        if node2.next != None:
            node3 = node2.next
            self.back(node1, node2, node3)
        else:
            node2.next = node1
            self.result = node2
            return
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        if head.next.next == None:
            new_head = head.next
            new_head.next = head
            head.next = None
            return new_head
        # >= 3 nodes:
        start = head
        mid = head.next
        end = mid.next
        start.next = None
        self.back(start, mid, end)
        res = self.result
        return res

l1, l2, l3, l4, l5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
l1.next = l2
l2.next = None
# l2.next = l3
# l3.next = l4
l3.next = None

l4.next = l5
l5.next = None
print("old:")
print_linked_list(l1)

s = Solution()
new_head = s.reverseList(l1)


print("new:")
print(new_head)
print_linked_list(new_head)
