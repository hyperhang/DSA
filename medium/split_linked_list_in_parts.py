from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_ll(self, node):
        res = []
        while node != None:
            res.append(node.val)
            node = node.next
        print(res)
            
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        iter = head
        while iter != None:
            count += 1
            iter = iter.next
        avg = count//k # avg = 3//5 = 0
        remain = count - avg*k # number of list which len is avg + 1 , i.e: 3 - 0 =3
        r = remain
        res = []
        iter = head
        list_length = 0
        before_iter = None
        while iter != None:
            # start inner list
            if list_length == 0:
                res.append(iter)
                if before_iter:
                    before_iter.next = None
            
            list_length += 1
            
            # end inner list
            if remain != 0:
                if list_length == avg + 1:
                    remain -= 1
                    list_length = 0
            else:
                if list_length == avg:
                    list_length = 0
            before_iter = iter
            iter = iter.next
        if avg == 0:
            print("k - remain = ", k - r)
            for i in range( k - r):
                res.append(None)  
        for node in res:
            print('-'*30)
            if node != None:
                print(node.val)
                self.print_ll(node)
            else:
                print('[]')
        
        return res

s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
k = 5

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n10 = ListNode(10)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
k = 3

print(s.splitListToParts(n1, k)  )            
        