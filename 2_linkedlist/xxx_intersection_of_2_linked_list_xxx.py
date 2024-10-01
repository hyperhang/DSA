# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(M+N)
# Space: O(M)
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
#         A = headA
#         B = headB
#         ref_b = set()
#         while B!= None:
#             ref_b.add(id(B))
#             B = B.next
#         conductor = headA
#         while conductor!= None:
#             print("- ",conductor.val)
#             if id(conductor) in ref_b :
#                 print("return value: ", conductor.val)
#                 return conductor
#             conductor = conductor.next        
#         return None

# Time: O(M+N)
# Space: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        leng_a, leng_b = 0, 0
        A, B = headA, headB
        
        while A!= None:
            leng_a += 1
            A = A.next          
        while B!= None:
            leng_b += 1
            B = B.next
        head_longer, head_shorter = None, None
        head_longer = headA if leng_a > leng_b else headB
        head_shorter = headB if leng_a > leng_b else headA
        move = max(leng_a, leng_b) - min(leng_a, leng_b)
        while move > 0:
            head_longer = head_longer.next    
            move -= 1
        while head_longer != None:
            if head_longer == head_shorter:
                return head_longer
            head_longer = head_longer.next
            head_shorter = head_shorter.next
               
        return None

l1 = ListNode(4)
l2 = ListNode(1)
l1.next = l2

k1 = ListNode(5)
k2 = ListNode(6)
k3 = ListNode(1)
k1.next = k2
k2.next = k3

m1 = ListNode(8)
m2 = ListNode(4)
m3 = ListNode(5)
m1.next = m2
m2.next = m3


l2.next = m1
k3.next = m1

s = Solution()
first_mutual_node = s.getIntersectionNode(l1, k1)
print(first_mutual_node == m1)
print(first_mutual_node.val == m1.val)
