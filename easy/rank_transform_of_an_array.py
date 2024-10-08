from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        dup = arr
        dup = sorted(dup)
        map = dict()
        c = 1
        map[dup[0]] = c
        for i in range(1,len(dup)):
            if dup[i] != dup[i-1]:
                c += 1
            map[dup[i]] = c
        ans = []
        for ele in arr:
            ans.append(map[ele])
        return ans
                
                
            
        
sol = Solution()
print(sol.arrayRankTransform([40,10,20,30]))
print(sol.arrayRankTransform([100,100,100]))
print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))