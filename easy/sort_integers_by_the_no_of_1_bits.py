from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bits = [[] for _ in range(15)]
        for num in arr:
            bits[bin(num).count("1")].append(num)
        print(bits)
            
        new_arr = []
        for sub_ar in bits:
            if len(sub_ar):
                new_arr += sorted(sub_ar)
        return new_arr
    
sol = Solution()
arr = [0,1,2,3,4,5,6,7,8]
arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(sol.sortByBits(arr))