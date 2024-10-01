from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        res = []
        count = 1
        row = []
        for i in original:
            if count <= n:
                pass
            else:
                count = 1
                res.append(row)
                row = []
            row.append(i)
            count += 1
            print("row: ", row)
        res.append(row)
        return res
    
s = Solution()

# original = [1,2,3,4]
# m = 2
# n = 2
original = [1,2]
m = 1
n = 1

print(s.construct2DArray(original,m,n))