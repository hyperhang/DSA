
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    result = []
    def postorder(self, root: 'Node') -> list:
        def check_node(root):
            if root:
                if root.children:
                    for child in root.children:
                        check_node(child)
                self.result.append(root.val)
        check_node(root)
        return self.result
        
n1 = Node(1)        
n2 = Node(2)        
n3 = Node(3)        
n4 = Node(4)        
n5 = Node(5)        
n6 = Node(6)        
n7 = Node(7)        
n8 = Node(8)        
n9 = Node(9)        
n10 = Node(10)        
n11 = Node(11)        
n12 = Node(12)        
n13 = Node(13)        
n14 = Node(14)        

# n1.children = [n2, n3, n4, n5]
# n3.children = [n6, n7]
# n4.children = [n8]
# n5.children = [n9, n10]
# n7.children = [n11]
# n8.children = [n12]
# n9.children = [n13]
# n11.children = [n14]

s = Solution()
print(s.postorder(Node()))