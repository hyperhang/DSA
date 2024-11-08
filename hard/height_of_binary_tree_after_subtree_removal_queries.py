from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeQueries( self, root: Optional[TreeNode], queries: List[int] ) -> List[int]:
        # Find all nodes in all longest paths, and find the longest path length (we call it X set), 
        # If query a node which is not in X, return the longest path length
        # If query a node which is in X:
        #   If that node have neighbors (neighbor is node having same level, and it is in one of the longest paths), return the longest path length
        #   else: check if there are any nodes which are the same level (but not neighbors), and check the node which has longest length to its leaf.
        
        levels = [root]
        parents = {}
        height = {}
        height[root] = 0
        get_node = {}
        count = 0
        last_level = [root]
        nodes_by_level = []
        
        while levels:
            next_level = []
            count += 1
            nodes_by_level.append(set(levels))
            for node in levels:
                get_node[node.val] = node
                if node.left:
                    parents[node.left] = node
                    height[node.left] = count
                    next_level.append(node.left)
                if node.right:
                    parents[node.right] = node
                    height[node.right] = count
                    next_level.append(node.right)
            if not next_level:
                last_level = levels
            levels = next_level
        
        nodes_in_longest_path = set()
        neighbors = {}
        cur_children = last_level
        while cur_children:
            next_children = set()
            for node in cur_children:
                neighbors[node] = 1 if len(cur_children) != 1 else 0
                print(f"{node.val} has neighbor: {neighbors[node]}")
                nodes_in_longest_path.add(node)
                if node in parents:
                    next_children.add(parents[node])
                else:
                    next_children = []
            cur_children = next_children
        
        ans = {}
        height_next = {}
        for i in range(len(nodes_by_level)-1, -1, -1):
            levels = nodes_by_level[i]
            height_next_max = 0
            flag = False
            for node in levels:
                if node not in nodes_in_longest_path:
                    flag = True
                    height_next[node] = 0
                    if node.left :
                        height_next[node] = 1 + height_next[node.left]
                    if node.right:
                        height_next[node] = max(1+height_next[node.right], height_next[node])
                    height_next_max = max(height_next_max, height_next[node])
            for node in levels:
                if node in nodes_in_longest_path:
                    if neighbors[node]:
                        ans[node] = count - 1
                    else:
                        if flag:
                            ans[node] = height_next_max + height[node]
                        else:
                            ans[node] = height[node] - 1
                    
            
        print("most longest path length: ", count-1) 

        result = []
        for val in queries:
            node = get_node[val]
            if node in nodes_in_longest_path:
                result.append(ans[node])
            else:
                result.append(count-1) # insert the longest path's length
        return result

sol = Solution()

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n8 = TreeNode(8)
# n9 = TreeNode(9)
# n5.left, n5.right = n8, n9
# n8.left, n8.right = n2, n1
# n9.left, n9.right = n3, n7
# n2.left, n2.right = n4, n6
# queries = [3,2,4,8]
# root = n5

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
# n1.left, n1.right = n3, n4
# n3.left = n2
# n4.left, n4.right = n6, n5
# n5.right = n7
# queries = [4]
# root = n1




# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n1.right = n5
# n5.left = n3
# n3.left , n3.right = n2, n4
# queries = [3,5,4,2,4]
# root = n1


# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n2.left, n2.right = n1, n5
# n5.left , n5.right = n3, n6
# n3.right = n4
# queries = [5,5,1,6,4,5]
# root = n2


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)
n12 = TreeNode(12)
n13 = TreeNode(13)
n14 = TreeNode(14)
n15 = TreeNode(15)
n16 = TreeNode(16)
n17 = TreeNode(17)
n18 = TreeNode(18)
n2.left, n2.right = n1, n7
n7.left, n7.right = n6, n10
n6.left = n5
n5.left = n4
n4.left = n3
n10.left, n10.right= n9, n16
n9.left = n8
n16.left, n16.right = n13, n17
n13.left, n13.right = n12, n14
n17.right = n18
n12.left = n11
n14.right = n15
root = n2
queries = [17,5,14,7,13,7,16,12,15,1,8,6,1,12,3,1,17,11]


sol = Solution()
print(sol.treeQueries(root, queries))
