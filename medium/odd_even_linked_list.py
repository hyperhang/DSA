class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printll(self, node):
        res = []
        while node != None:
            res.append(node.val)
            node = node.next
        print(res)
        
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: # 0
            return None
        if head.next == None: # 1
            self.printll(head)
            return head
        if head.next.next == None : #2
            self.printll(head)
            return head
        self.printll(head)
        i = 3
        first_odd = head
        # last_odd = head
        first_even = head.next
        t1 = first_odd
        t2 = first_even
        # last_even = first_even
        iter = head.next.next
        while iter != None:
            if i%2 == 1:
                first_odd.next = iter
                first_odd = first_odd.next
                print("odd: ", first_odd.val)
            else:
                first_even.next = iter
                first_even = first_even.next
                print("even: ", first_even.val)
            i += 1
            iter = iter.next
            
        first_odd.next = t2
        first_even.next = None
        self.printll(t1)
        return t1
    
s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
  
# n1.next = n2          
# n2.next = n3          
# n3.next = n4          
# n4.next = n5 

n2.next = n1
n1.next = n3
# n3.next = n5
# n5.next = n6
# n6.next = n4
# n4.next = n7   

s.oddEvenList(n2)      
        