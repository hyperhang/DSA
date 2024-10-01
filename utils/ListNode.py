class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def make_ll_from_array(ar:list)  :
        if len(ar) == 0:
            return "can't make LL from array"
        head = ListNode(ar[0])
        current = head
        for val in ar[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    @staticmethod
    def print_ll(head):
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        print(res)

ll = ListNode()
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
iter = ll.make_ll_from_array(head)
ll.print_ll(iter)

        
        