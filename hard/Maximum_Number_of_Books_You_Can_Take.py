from typing import List

# TLE : O(n^2)
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        def get_sum_des(idx):
            cur = books[idx]
            su = 0
            while idx >=0 and cur > 0:
                su += cur
                if idx == 0:
                    return su
                cur = min(books[idx-1], cur-1)
                idx -= 1
            return su
        answer = 0
        for i in range(len(books)-1, -1, -1):
            t = get_sum_des(i)
            answer = max(answer, t)
        return answer
    
# Next smaller (monotonic stack), dp, BS
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        def find_NSE(books: list, n:int):
            # next small element
            next_smaller = [None]*n
            values = []
            indexes = []
            for idx, ele in enumerate(books):
                if len(values) > 0 and ele < values[-1]:
                    while len(values) > 0 and ele < values[-1]:
                        next_smaller[indexes[-1]] = idx
                        values.pop()
                        indexes.pop()
                    values.append(ele)
                    indexes.append(idx)
                else:
                    values.append(ele)
                    indexes.append(idx)
            return next_smaller
        
        reversed_books = books.reverse()
       
        right_smaller = find_NSE(reversed_books,n)
        left_smaller = [-1]*n
        for i in range(len(right_smaller) ):
            new_val = n-1 - right_smaller[i] if right_smaller[i] != None else None
            left_smaller[ n-1 - i] = new_val
        
        dp = [] 
        ma = 0 
        for i, ele in enumerate(books):
            if left_smaller[i] == None:
                temp_index = i - (ele - 1)
                _sum = None
                if temp_index < 0:
                    start = ele - i
                    end = ele
                    _sum = (start+end)*(i+1)//2
                else:
                    _sum = (1+ele)*ele//2
                ma = max(ma, _sum)
            else:
                
             
        

    
s = Solution()
books = [8,5,2,7,9]
#  1 2 3 4 5 6
books = [7,0,3,4,5]
books = [8,2,3,7,3, 4,0,1,4,3]
# books = [8,3]
print(s.maximumBooks(books))

# 8 2, 0 1
# -> 8: 2, 0: 1
# -> 8, 0
# 2 3 7 3, 1 2 3 4
# -> 7: 3, 3: 4
# -> 2 3 3
# 2 3 3 4   0,  1 2 4 5   6
# ->  4: 0
# 2 3 3 0
# -> 3: 0
# 2 3 0
# -> 3: 0
# 2 0
# -> 2: 0
# 0
# 0 1 4 3
# -> 4: 3
# 0 1 3



                