from typing import List, Optional
from utils.ListNode import ListNode

class Solution:
    # def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    #     matrix = [ [-1]*n for _ in range(m) ]
        
    #     def fill(x, y, m, n, iter: Optional[ListNode]):
    #         if m < 1 or n < 1:
    #             return
    #         # x: start from x to x+m
    #         # y: start from y to y+n
    #         for i in range(n):
    #             val = iter.val if iter != None else -1
    #             matrix[x][y+i] = val
    #             iter = iter.next if iter else None
    #         if m == 1:
    #             return
    #         for i in range(1, m):
    #             val = iter.val if iter != None else -1
    #             matrix[x+i][y+n-1] = val
    #             iter = iter.next if iter else None
    #         if n == 1:
    #             return
    #         for i in range(n-2, -1, -1):
    #             val = iter.val if iter != None else -1
    #             matrix[x+m-1][y+i] = val
    #             iter = iter.next if iter else None
    #         for i in range(m-2, 0, -1):
    #             val = iter.val if iter != None else -1
    #             matrix[x+i][y] = val
    #             iter = iter.next if iter else None
            
    #         fill(x+1, y+1, m-2, n-2, iter)
                
    #     fill(0,0, m,n, head)
    #     print("Matrix: ")
    #     for i in range(m):
    #         print(matrix[i])
    #     return matrix

    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        # Store the east, south, west, north movements in a matrix.
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        current_d = 0
        matrix = [ [-1]*n for _ in range(m) ]
        i, j = 0, 0
        while head != None:
            val = head.val
            matrix[i][j] = val
            newi = i + direction[current_d][0]
            newj = j + direction[current_d][1]
            
            # When direction changes:
            if newi <0 or newj <0 or newi > m-1 or newj > n-1 or matrix[newi][newj] != -1:
                current_d = (current_d + 1)%4
                
            i += direction[current_d][0]
            j += direction[current_d][1]

            head = head.next
            
        print("Matrix: ")
        for i in range(m):
            print(matrix[i])
            
        return matrix
            
s = Solution()

m = 1
n = 4
head = [0,1,2,-1]

# m = 3
# n = 5
# head = [3,0,2,6,8,1,7,9,4,2,5,5,0]

# m=4
# n = 1
# head = [2,1]

n0 = ListNode.make_ll_from_array(head)
s.spiralMatrix(m,n,n0)
            