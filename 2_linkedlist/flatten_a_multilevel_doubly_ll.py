# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        
def print_linked_list(head: Node):
    origin = head
    last_node = None
    print("forward:")
    while head!=None:
        print(head.val, end = ", ")
        if head.next == None:
            last_node = head
            break
        head = head.next
    print()
    
    print("backward:")
    while last_node!=None:
        print(last_node.val, end = ", ")
        last_node = last_node.prev
    print()    
    
        
class Solution:        
    def flatten(self, head: Node) -> Node:
        start = head
        tem = None
        def check_child(node: Node):
            # Với mỗi node , tìm ref của last_child của nó, rồi gán last_child.next bằng node.next , và node.next.prev = last_child. Sau đó bắt đầu vòng lặp mới cho node.next 
            if node == None:
                print("r: node = None")
                return None
            child = node.child
            right = node.next
            last_child = None
            if child == None:
                if right == None:
                    print("r: ", node.val)
                    self.tem = node
                    return node # last child's node
                else:
                    print("recursion, child == None, start at: ", right.val)
                    return check_child(right)
            else: # child != None
                first_child = child
                first_child.prev = node
                node.next = first_child
                node.child = None
                
                last_child = check_child(first_child)
                
                # check_child(first_child)
                # last_child = self.tem
                
                print(f"last_child: {last_child}")
                if right != None :
                    right.prev = last_child
                    last_child.next = right
                    print("recursion, child != None, start at: ", right.val)
                    return check_child(right)
                else:
                    print("r: ...")
                    return None
                        
        check_child(head)
        return start
    
s = Solution()
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12 = Node(1, None, None, None),Node(2, None, None, None), Node(3, None, None, None),Node(4, None, None, None), Node(5, None, None, None), Node(6, None, None, None),Node(7, None, None, None), Node(8, None, None, None),Node(9, None, None, None),Node(10, None, None, None), Node(11, None, None, None), Node(12, None, None, None)

n1.next, n2.next, n3.next, n4.next, n5.next,    n7.next, n8.next, n9.next,      n11.next    =    n2, n3, n4, n5, n6,       n8, n9, n10,    n12
n2.prev, n3.prev, n4.prev, n5.prev, n6.prev,    n8.prev, n9.prev, n10.prev,     n12.prev    =    n1, n2, n3, n4, n5,       n7, n8, n9,      n11  
n3.child , n8.child = n7, n11

start = s.flatten(n1)
print_linked_list(start)
