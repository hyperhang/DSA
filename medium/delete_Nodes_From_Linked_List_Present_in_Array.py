# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def print_ll(self, head: ListNode):
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        print(res)
            
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        iter1 = head
        self.print_ll(head)
        while iter1 != None:
            if iter1.val in nums:
                iter1 = iter1.next
            else:
                break
        print("start: ", iter1.val)     
        head = iter1   
        iter2 = iter1.next
        # 
        
        while iter2 != None:
            current_val = iter2.val
            if current_val in nums:
                # need to remove this node
                print("removed: ", current_val)
                iter1.next = iter2.next
            else:
            # ignore, move next
                iter1 = iter2
            iter2 = iter1.next
        
        self.print_ll(head)
        return head

s= Solution()

nums = [1,2,3]

head = [1,2,3,4,5,2,2]  
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n2_1 = ListNode(2)
n2_2 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2_1
n2_1.next = n2_2

s.modifiedList(nums, n1)
         